

# crossing number test for a point in a polygon
# Input:   p: a point,
#          verts: vertex points of a polygon verts[n+1] with verts[n]=V[0]
# Return:  False = outside, True = inside
#  This code is patterned after [Franklin, 2000]
def point_in_poly_cn(p, verts):

    # the crossing number counter
    cn = 0

    for i in range(0, len(verts)-1):
        y1 = verts[i][1]
        y2 = verts[i+1][1]
        if ((y1 <= p[1] and y2 > p[1]) or (y1 > p[1] and y2 <= p[1])):
            
            # compute the actual edge-ray intersect x-coordinate
            vt = (p[1] - y1) / (y2 - y1)

            x1 = verts[i][0]
            x2 = verts[i+1][0]
            if (p[0] < x1 + vt * (x2-x1)):
                cn += 1
    
    return bool(cn & 1)


# is_left(): tests if a point is Left|On|Right of an infinite line.
# Input: three points P0, P1, and P2
# Return: >0 for P2 left of the line through P0 and P1
#         =0 for P2  on the line
#         <0 for P2  right of the line
def is_left(p0, p1, p2):
    return ( (p1[0] - p0[0]) * (p2[1] - p0[1])
            - (p2[0] -  p0[0]) * (p1[1] - p0[1]) )


# winding number test for a point in a polygon
# Input:   p: a point,
#          verts: vertex points of a polygon verts[n+1] with verts[n]=verts[0]
# Return:  False = outside, True = inside
def point_in_poly_wn(p, verts):

    # the winding number counter
    wn = 0
    
    for i in range(0, len(verts)-1):
        y = p[1]
        if (verts[i][1] <= y):
            if (verts[i+1][1] > y):
                if (is_left(verts[i], verts[i+1], p) > 0):
                    wn += 1
        else:
            if (verts[i+1][1] <= y):
                if (is_left(verts[i], verts[i+1], p) < 0):
                    wn -= 1

    return wn != 0
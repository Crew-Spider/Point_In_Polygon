from draw_image import draw_polygon, draw_polygon_and_inoutside_points
from generate_polygon import generate_polygon, generate_points
from point_in_poly import point_in_poly_cn, point_in_poly_wn
import time



def test_draw():
    draw_polygon(
        generate_polygon( 
            ctrX=250, ctrY=250, 
            aveRadius=100, irregularity=0.35, 
            spikeyness=0.2, numVerts=16 
        )
    )


if __name__ == "__main__":

    # 生成多边形详情请见generate_polygon.py
    verts = generate_polygon( 
        ctrX=500, ctrY=500, 
        aveRadius=280, irregularity=0.35, 
        spikeyness=0.2, numVerts=100 
    )
    
    verts.append(verts[0])

    inside_points = []
    outside_points = []

    # 修改第一个参数，设置点的数量
    points = generate_points(100000, x_range=(100, 900), y_range=(100, 900))

    #############################################
    # 算法对比
    #############################################
    # start = time.time()
    # for point in points:
    #     point_in_poly_cn(point, verts)
    # end = time.time()
    # print("the crossing number: " + str(end-start) + " s")

    # start = time.time()
    # for point in points:
    #     point_in_poly_wn(point, verts)
    # end = time.time()
    # print("the winding number: " + str(end-start) + " s")
    
    
    #############################################
    # 画图
    #############################################
    start = time.time()
    for point in points:
        if point_in_poly_wn(point, verts):
            inside_points.append(point)
        else:
            outside_points.append(point)
    end = time.time()
    print("the winding number: " + str(end-start) + " s")
    
    draw_polygon_and_inoutside_points(verts, inside_points, outside_points, (1000, 1000))
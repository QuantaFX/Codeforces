def sol():
    px, py, qx, qy, rx, ry, sx, sy = map(int, input().split())

    pq_x = qx - px
    pq_y = qy - py

    rs_x = sx - rx
    rs_y = sy - ry

    cross = (pq_x * rs_y) - (pq_y * rs_x)

    if cross != 0:
        print("Yes")
    else:
        m_x = (rx + sx) - (px + qx)
        m_y = (ry + sy) - (py + qy)
        dot = (m_x * pq_x) + (m_y * pq_y)

        if dot != 0:
            print("No")
        else:
            print("Yes")

tc = int(input())
while tc:
    tc -= 1
    sol()
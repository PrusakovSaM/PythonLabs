import turtle as t

lng = 50
num = [
    [(0, -2 * lng), (-lng, 0), (0, 2 * lng), (lng, 0)],
    [(-lng, -lng), (lng, lng), (0, -2 * lng), (0, 2 * lng)],
    [(-lng, 0), (lng, 0), (0, -lng), (-lng, -lng),
         (lng, 0), (-lng, 0), (lng,lng), (0, lng)],
    [(-lng, 0), (lng, 0), (-lng, -lng), (lng, 0),
         (-lng, -lng), (lng, lng), (-lng, 0), (lng, lng)],
    [(0, -2 * lng), (0, lng), (-lng, 0),
         (0, lng), (0, -lng), (lng, 0), (0, lng)],
    [(-lng, 0), (0, -lng), (lng, 0), (0, -lng),
         (-lng, 0), (lng, 0), (0, lng), (-lng, 0), (0, lng), (lng, 0)],
    [(-lng, -lng), (0, -lng), (lng, 0), (0, lng), (-lng, 0), (lng, lng)],
    [(-lng, 0), (lng, 0), (-lng, -lng), (0, -lng), (0, lng), (lng, lng)],
    [(-lng, 0), (0, -lng), (lng, 0), (0, -lng),
         (-lng, 0), (0, lng), (lng, 0), (0, lng)],
    [(-lng, 0), (0, -lng), (lng, 0), (-lng, -lng), (lng, lng), (0, lng)]
    ]

pos = [-6 * lng, lng]


def draw_num(n):
    global pos
    for i in num[n]:
        pos[0] += i[0]
        pos[1] += i[1]
        t.goto(*pos)
    t.penup()
    pos[0] += 1.5 * lng
    t.goto(*pos)
    t.pendown()


num_inp = input("Индекс: ")

t.shape("turtle")

t.penup()
t.goto(*pos)
t.pendown()

for i in num_inp:
    draw_num(int(i))

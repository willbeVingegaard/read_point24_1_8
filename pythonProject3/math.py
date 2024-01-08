import turtle as t
list=[[41.0, 49.0], [35.0, 17.0], [55.0, 45.0], [55.0, 20.0], [15.0, 30.0], [25.0, 30.0], [20.0, 50.0], [10.0, 43.0], [55.0, 60.0], [30.0, 60.0], [20.0, 65.0], [50.0, 35.0], [30.0, 25.0], [15.0, 10.0], [30.0, 5.0], [10.0, 20.0], [5.0, 30.0], [20.0, 40.0], [15.0, 60.0], [45.0, 65.0], [45.0, 20.0], [45.0, 10.0], [55.0, 5.0], [65.0, 35.0], [65.0, 20.0], [45.0, 30.0], [35.0, 40.0], [41.0, 37.0], [64.0, 42.0], [40.0, 60.0], [31.0, 52.0], [35.0, 69.0], [53.0, 52.0], [65.0, 55.0], [63.0, 65.0], [2.0, 60.0], [20.0, 20.0], [5.0, 5.0], [60.0, 12.0], [40.0, 25.0], [42.0, 7.0], [24.0, 12.0], [23.0, 3.0], [11.0, 14.0], [6.0, 38.0], [2.0, 48.0], [8.0, 56.0], [13.0, 52.0], [6.0, 68.0], [47.0, 47.0], [49.0, 58.0], [27.0, 43.0], [37.0, 31.0], [57.0, 29.0], [63.0, 23.0], [53.0, 12.0], [32.0, 12.0], [36.0, 26.0], [21.0, 24.0], [17.0, 34.0], [12.0, 24.0], [24.0, 58.0], [27.0, 69.0], [15.0, 77.0], [62.0, 77.0], [49.0, 73.0], [67.0, 5.0], [56.0, 39.0], [37.0, 47.0], [37.0, 56.0], [57.0, 68.0], [47.0, 16.0], [44.0, 17.0], [46.0, 13.0], [49.0, 11.0], [49.0, 42.0], [53.0, 43.0], [61.0, 52.0], [57.0, 48.0], [56.0, 37.0], [55.0, 54.0], [15.0, 47.0], [14.0, 37.0], [11.0, 31.0], [16.0, 22.0], [4.0, 18.0], [28.0, 18.0], [26.0, 52.0], [26.0, 35.0], [31.0, 67.0], [15.0, 19.0], [22.0, 22.0], [18.0, 24.0], [26.0, 27.0], [25.0, 24.0], [22.0, 27.0], [25.0, 21.0], [19.0, 21.0], [20.0, 26.0], [18.0, 18.0]]
list_data= [[41.0, 49.0], [35.0, 17.0], [55.0, 45.0], [55.0, 20.0], [15.0, 30.0], [25.0, 30.0], [20.0, 50.0], [10.0, 43.0], [55.0, 60.0], [30.0, 60.0], [20.0, 65.0], [50.0, 35.0], [30.0, 25.0], [15.0, 10.0], [30.0, 5.0], [10.0, 20.0], [5.0, 30.0], [20.0, 40.0], [15.0, 60.0], [45.0, 65.0], [45.0, 20.0], [45.0, 10.0], [55.0, 5.0], [65.0, 35.0], [65.0, 20.0], [45.0, 30.0], [35.0, 40.0], [41.0, 37.0], [64.0, 42.0], [40.0, 60.0], [31.0, 52.0], [35.0, 69.0], [53.0, 52.0], [65.0, 55.0], [63.0, 65.0], [2.0, 60.0], [20.0, 20.0], [5.0, 5.0], [60.0, 12.0], [40.0, 25.0], [42.0, 7.0], [24.0, 12.0], [23.0, 3.0], [11.0, 14.0], [6.0, 38.0], [2.0, 48.0], [8.0, 56.0], [13.0, 52.0], [6.0, 68.0], [47.0, 47.0], [49.0, 58.0], [27.0, 43.0], [37.0, 31.0], [57.0, 29.0], [63.0, 23.0], [53.0, 12.0], [32.0, 12.0], [36.0, 26.0], [21.0, 24.0], [17.0, 34.0], [12.0, 24.0], [24.0, 58.0], [27.0, 69.0], [15.0, 77.0], [62.0, 77.0], [49.0, 73.0], [67.0, 5.0], [56.0, 39.0], [37.0, 47.0], [37.0, 56.0], [57.0, 68.0], [47.0, 16.0], [44.0, 17.0], [46.0, 13.0], [49.0, 11.0], [49.0, 42.0], [53.0, 43.0], [61.0, 52.0], [57.0, 48.0], [56.0, 37.0], [55.0, 54.0], [15.0, 47.0], [14.0, 37.0], [11.0, 31.0], [16.0, 22.0], [4.0, 18.0], [28.0, 18.0], [26.0, 52.0], [26.0, 35.0], [31.0, 67.0], [15.0, 19.0], [22.0, 22.0], [18.0, 24.0], [26.0, 27.0], [25.0, 24.0], [22.0, 27.0], [25.0, 21.0], [19.0, 21.0], [20.0, 26.0], [18.0, 18.0]]
t.goto(0,0)
t.forward(320)
t.goto(0,0)
t.left(90)
t.forward(320)
t.speed(0)
for i in range(len(list)):
    t.up()
    x_loc=list[i][0]
    y_loc=list[i][1]
    t.goto(x_loc*4,y_loc*4)
    t.down()
    t.dot(5,'blue')

for i in range(len(list_data)):
    t.up()
    x_loc=list_data[i][0]
    y_loc=list_data[i][1]
    t.goto(x_loc*4,y_loc*4)
    t.down()
    t.dot(5,'red')

t.done()
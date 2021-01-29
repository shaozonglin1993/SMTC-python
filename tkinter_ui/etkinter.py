
#!/usr/bin/python3
 
from tkinter import *
root = Tk()                     #创建窗口对象的背景色

#创建两个列表
li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = Listbox(root)          #  创建两个列表组件
listb2 = Listbox(root)
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)
 
for item in movie:              # 第二个小部件插入数据
    listb2.insert(0,item)
 
listb.pack()                    # 将小部件放置到主窗口中
listb2.pack()


# 进入消息循环
root.mainloop()

#---------------------------------------------------------------

root = Tk()

root.title('missWjz')

cv = Canvas(root,background='white',width=830,height=830)
cv.pack(fill=BOTH,expand=YES)

#对字体进行初始化，字体样式，字体大小，字体是否加粗
columnFont = ('微软雅黑',18)
titleFont = ('微软雅黑',15,'bold')

#采用循环打印字体
for i,str in enumerate(['默认', '指定边宽', '指定填充', '边框颜色', '位图填充']):
    cv.create_text((130 + i*140,20),text=str,
                   font = columnFont,   #字体
                   fill = 'red',        #填充颜色
                   anchor = W,          #对齐方式
                   justify = LEFT
                   )


#绘制字体
cv.create_text((10,80),text="绘制矩形",
               font = titleFont,
               fill = 'blue',
               anchor = W,
               justify = LEFT
            )

#创建列表：图形边框大小 填充色 边框颜色 位图填充
options = [(None,None,None,None),
           (4,None,None,None),
           (4,'pink',None,None),
           (4,'pink','red',None),
           (4,'pink','red','error')]

#创建矩形图案
for i,opt in enumerate(options):
    cv.create_rectangle((130+i*140,50,240+i*140,120),
                        width = opt[0],     #边框宽度
                        fill = opt[1],      #图案填充色
                        outline = opt[2],   #图案边框颜色
                        stipple = opt[3]    #位图填充
                        )

#绘制字体
cv.create_text((10,190),text='绘制椭圆',
               font = titleFont,
               fill = 'blue',
               anchor = W,
               justify = LEFT
               )

#绘制椭圆
for i,opt in enumerate(options):
    cv.create_oval((130+i*140,150,240+i*140,220),
                   width = opt[0],
                   fill = opt[1],
                   outline = opt[2],
                   stipple = opt[3])

#绘制文字
cv.create_text((10,300),text='绘制多边形',
               font = titleFont,
               fill = 'blue',
               anchor = W,
               justify = LEFT)

#绘制 五角星
for i,opt in enumerate(options):
    cv.create_polygon((130+i*140,270,240+i*140,270,152+i*140,350,185+i*140,230,218+i*140,350,130+i*140,270),
                      width = opt[0],
                      fill = opt[1],
                      outline = opt[2],
                      stipple = opt[3])

#绘制文字
cv.create_text((10,410),text='绘制扇形',
               font = titleFont,
               fill = 'blue',
               anchor = W,
               justify = LEFT)

#绘制扇形 提供两个坐标
for i,opt in enumerate(options):
    cv.create_arc((130+i*140,380,240+i*140,460),
                  width = opt[0],
                  fill = opt[1],
                  outline = opt[2],
                  stipple = opt[3],
                  )

#绘制文字
cv.create_text((10,520),text='绘制弓形',
               font = titleFont,
               fill = 'blue',
               anchor = W,
               justify = LEFT)
#绘制弓形
for i,opt in enumerate(options):
    cv.create_arc((130+i*140,490,240+i*140,570),
                  width = opt[0],
                  fill = opt[1],
                  outline = opt[2],
                  stipple = opt[3],
                  start = 30,   #起始角度
                  extent = 180, #逆时针转过角度
                  style =  CHORD    #弓张开的方式
                  )

#绘制文字
cv.create_text((10,630),text='仅绘弧',
               font = titleFont,
               fill = 'blue',
               anchor = W,
               justify = LEFT)
#仅绘制弧
for i,opt in enumerate(options):
    cv.create_arc((130+i*140,600,240+i*140,680),
                  width = opt[0],
                  fill = opt[1],
                  outline = opt[2],
                  stipple = opt[3],
                  start = 30,   #起始角度
                  extent = 180, #逆时针转过角度
                  style =  ARC    #弓张开的方式
                  )
#绘制文字
cv.create_text((10,740),text='绘制直线',
               font = titleFont,
               fill = 'blue',
               anchor = W,
               justify = LEFT)
#绘制直线
options = [(None,None,None,None,None),
           (6,None,None,BOTH,(20,40,10)),   #BOTH：两头都有箭头;长度，箭头长度，宽度
           (6,'pink',None,FIRST,(40,40,10)),
           (6,'pink',None,LAST,(60,50,10)),
           (8,'pink','error',None,None)]

for i,opt in enumerate(options):
    cv.create_line((130+i*140,710,240+i*140,790),
                   width = opt[0],
                   fill = opt[1],
                   stipple = opt[2],
                   arrow = opt[3],
                   arrowshape=opt[4]#arroeshape形如 "20 20 10" 的字符串,字符串中的三个整数依次指定填充长度、箭头长度、箭头宽度
                   )

root.mainloop()

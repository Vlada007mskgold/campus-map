import datetime # засекаем время работы кода
d1 = datetime.datetime.today()
"""""
===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   
                                                                                                       ПОДГОТОВКА К НАПИСАНИЮ КОДА
===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   
"""""



# ===== ========== ПОДГОТОВКА К НАПИСАНИЮ ========== =====
import math # мат функции
import pygame as pygame # пугаме
#import datetime # засекаем время работы кода
pygame.init() # разрешаем доступ к пугаму
window = pygame.display.set_mode((1536, 720)) # окошко
window.fill( (255, 255, 255) ) # рисуем окошко
pygame.display.update() # обновляем моник
from pygame.locals import * # букафки пугама
stile = pygame.font.Font(None, 30) # создаём свой шрифт
# ========== ========== ========== ========== ==========



"""""
===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   
                                                                                                                КЛАССЫ
===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   
"""""



# =============== ======= =============== КЛАСС КАРТИНОК =============== ======= ===============
class PNG():
    def __init__(self, x, y, x0, y0, png_name, unicuie_name):
        self.x = x # левая грань
        self.y = y # верхняя грань
        self.x0 = x0 # ширина картинки
        self.y0 = y0 # высота картинки
        self.png_name = png_name # имя картинки
        self.unicuie_name = unicuie_name # название объекта
        self.surf = pygame.image.load(png_name) # открываем картинку
        self.cords = self.surf.get_rect( bottomright=(x0+x,y0+y) ) # выбираем область на картинке
    def draw(self): # нарисовать
        window.blit(self.surf, self.cords)
# =============== =============== =============== =============== =============== ===============



# =============== ============= КЛАСС КНОПОК ============= =============
class Button():
    def __init__(self, png): 
        self.png = png # изображение кнопки
        self.x = png.x # левая грань
        self.y = png.y # верхняя грань
        self.name = png.unicuie_name # имя кнопки
        self.w = png.x0 # ширина кнопки
        self.h = png.y0 # высота кнопки
    def pressed(self, click): # возвращает 1 если кнопка нажата. 0-иначе
        if self.x < click[0] < (self.x + self.w):
            if self.y < click[1] < (self.y + self.h): return True
            else: return False
        else: return False

    def draw(self): # рисует кнопку  
        self.png.draw()
# ================ ================== ================== ================



# ================ ================== ================== ================== КЛАСС ДОРОГ ================== ================== ================== ================
class route():
    def __init__(self, start, finish): # начальные и конечные точки подаются на вход
        global dict_rooms # вызываем первичный словарь
        self.start = dict_rooms[start] # пункт начала
        self.finish = dict_rooms[finish] # пункт конца
    def draw(self): # рисовашка
        pygame.draw.lines(window, (50, 200, 80), True, [ [self.start.x,self.start.y], [self.finish.x,self.finish.y] ], 4) # рисуем прямую между началом и концом
# ================ ================== ================== ================ ================ ================ ================== ================== ================        



# ===================== ========== ===================== ======== КЛАСС КАБИНЕТОВ ======== ===================== ========== =====================
class room():
    def __init__(self, name, x, y): # координаты начала отсчёта
        if name == '8.119': self.name = 'стол зел'
        elif name == '8.118': self.name = 'стол гол'
        else: self.name = name
        self.x = int(x)
        self.y = int(y)        
# ======================= ======================= ======================= ======================= ======================= =======================



"""""
===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   
                                                                                                                ФУНКЦИИ
===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   
"""""



# ============================== ============================== ============================== ======== ПОИСК МАРШРУТА С ПРОМЕЖУТКАМИ ======== ============================== ============================== ==============================
def from_to(start, finish, remarks): # старт, финишь, [п1, п2,..., пn]                        | это полу-рекурсивная функция, работающая по следуйщему принцыпу:
    global processed # из глобальной базы переменных вызываем третичный словарь               | если нет промежуточных пунктов - то выполняется линейная часть функции,
    if len(remarks) == 0: # если нет промежуточных пунктов                                    | то бишь она просто в памяти находит кратчайший маршрут между пунктами.
        for i_0007 in processed: # рассматриваем ВСЕ маршруты                                 | если же промежуточные пункты есть, то всё немного сложнее:
            if start in i_0007: # если в этом маршруте есть пункт старта                      | сначала при помощи постоянных вызываний линейной части функции с нуля строится маршрут через все промежуточные пункты.
                if finish in i_0007: # если в этом маршруте есть пункт финиша                 | заметка: в идеале надо сделать функцию, которая правильным(наиболие удобным) образом сортирует промежуточные пункты.
                    road = list(map(str, i_0007.split('_'))) # [старт, п1, п2,..., пn, финиш] | потом происходит просто приведение дороги в адекватный вид
                    if road[0] == start: # если начальный пункт маршрута - старт              | и в итоге, в любом случае, функция возвращает дорогу и её длину.
                        if road[-1] == finish: # если конечный пункт маршрута - финиш         |_____________________________________________________________________________________________________________________________________________
                            return (i_0007, int(processed[i_0007])) # возвращаем маршрут и его длину              
                            break # завершраем работу цыкла поиска, а после неё завершается и работа функции

    else: # если есть промежуточные пункты                                                                   
        road = '' # маршрут                                                           
        lenght = 0 # длинамаршрута                                                         
        for i_0008 in range(len(remarks)): # рассматриваем номера промежуточных пунктов в ихнем списке                                 
            if i_0008 != 0: # если мы не рассматриваем нулевой пункт                                                 
                road += '_' # добавить разделительный знак                                                 
                (part, S) = from_to(remarks[i_0008-1], remarks[i_0008], []) # самоввызов функции(от предидущего пункта к нынешнему), но уже без промежуточных пунктов
            else: # если мы рассматриваем нулевой пункт                                                            
                (part, S) = from_to(start, remarks[0], []) # самоввызов функции(от старта к первому пункту), но уже без промежуточных пунктов             
            road += part # добавляем новый участок пути                                                    
            lenght += S # добавляем длину нового участка пути                                                     
        (part, S) = from_to(remarks[-1], finish, []) # самоввызов функции(от последнего пункта к финишу), но уже без промежуточных пунктов                        
        road += '_' + part # добавляем новый участок маршрута                                                  
        lenght += S # добавляем длину нового учатска пути                                                         
        r = list(map(str, road.split('_'))) # [старт, p1, p2,..., pt, финиш]                                 
        road = r[0] # итоговый маршрут                                                         
        i_past = r[0] # предидущий пункт маршрута                                                        
        for i_0009 in r[1::]: # рассматриваем все участки маршрута, начиная со второго                                                
            if i_0009 != i_past: road += '_' + i_0009 # если участок маршрута не идёт дважды подряд: добавить его в итоговый маршрут                       
            i_past = i_0009 # запоминаем "предыдущий" пункт                                                 
        return (road, int(lenght)) # возвращаем маршрут и его длину
# ============================== ============================== ============================== =============== ============================== ============================== ============================== ==============================            



# ================= =============== ВЫБОР НАЖАТОЙ КНОПКИ =============== =================
def button_select(button_list, mouse): # возвращает нажатую кнопку. если таковой нет - 'no'
    i_0011 = 0 # сколько просмотрели кнопок
    while i_0011 < len(button_list): # проверяем факт нажатия кнопок
        if button_list[i_0011].pressed(mouse): # если мышь в месте этой кнопки, то
            return button_list[i_0011] # возвращаем кнопку
            break 
        i_0011 += 1
    if i_0011 >= len(button_list): return 'no' # если таких кнопок не нашлось
# ================= ================= ================= ================= =================



# ============ КАКАЯ КЛАВИША НАЖАТА ============
def returner():
    if keys[pygame.K_q]: return 'й'
    elif keys[pygame.K_w]: return 'ц'
    elif keys[pygame.K_e]: return 'у'
    elif keys[pygame.K_r]: return 'к'
    elif keys[pygame.K_t]: return 'е'
    elif keys[pygame.K_y]: return 'н'
    elif keys[pygame.K_u]: return 'г'
    elif keys[pygame.K_i]: return 'ш'
    elif keys[pygame.K_o]: return 'щ'
    elif keys[pygame.K_p]: return 'з'
    elif keys[pygame.K_LEFTBRACKET]: return 'х'
    elif keys[pygame.K_RIGHTBRACKET]: return 'ъ'
    elif keys[pygame.K_a]: return 'ф'
    elif keys[pygame.K_s]: return 'ы'
    elif keys[pygame.K_d]: return 'в'
    elif keys[pygame.K_f]: return 'а'
    elif keys[pygame.K_g]: return 'п'
    elif keys[pygame.K_h]: return 'р'
    elif keys[pygame.K_j]: return 'о'
    elif keys[pygame.K_k]: return 'л'
    elif keys[pygame.K_l]: return 'д'
    elif keys[pygame.K_SEMICOLON]: return 'ж'
    elif keys[pygame.K_QUOTEDBL]: return 'э'
    elif keys[pygame.K_z]: return 'я'
    elif keys[pygame.K_x]: return 'ч'
    elif keys[pygame.K_c]: return 'с'
    elif keys[pygame.K_v]: return 'м'
    elif keys[pygame.K_b]: return 'и'
    elif keys[pygame.K_n]: return 'т'
    elif keys[pygame.K_m]: return 'ь'
    elif keys[pygame.K_COMMA]: return ','
    elif keys[pygame.K_PERIOD]: return '.'
    


    

    elif keys[pygame.K_1]: return '1'
    elif keys[pygame.K_2]: return '2'
    elif keys[pygame.K_3]: return '3'
    elif keys[pygame.K_4]: return '4'
    elif keys[pygame.K_5]: return '5'
    elif keys[pygame.K_6]: return '6'
    elif keys[pygame.K_7]: return '7'
    elif keys[pygame.K_8]: return '8'
    elif keys[pygame.K_9]: return '9'
    elif keys[pygame.K_0]: return '0'

    elif keys[pygame.K_PERIOD]: return '.'
    elif keys[pygame.K_RETURN]: return 'enter'
    elif keys[pygame.K_BACKSPACE]: return 'delet'
    elif keys[pygame.K_COMMA]: return ','
    elif keys[pygame.K_SPACE]: return ' '
# =============== =============== ===============



# раскодировщик
def uncoder():
    file = open('дороги.txt', 'r', -1, 'utf-8')
    dict_roads_ = {}
    while True:
        line = file.readline()
        if not line: break
        else:
            a = list(map(str, line.split(', ')))
            dict_roads_[a[0]] = a[1][0:-2]
    file.close()

    dict_rooms_ = {}
    file = open('комнаты.txt', 'r', -1, 'utf-8')
    while True:
        line = file.readline()
        if not line: break
        else:
            a = list(map(str, line.split(', ')))
            dict_rooms_[a[0]] = room(a[0], a[1], a[2])
    file.close()

    return (dict_roads_, dict_rooms_) 
#



#
def toilet(start, fact):
    global dict_rooms
    list_l = []
    list_n = []
    if fact: a = '6'
    else: a = '5'
    for j_0 in dict_rooms:
        if dict_rooms[j_0].name[0] == a:
            #print(start, dict_rooms[j_0].name)
            (n, s) = from_to(start, dict_rooms[j_0].name, [])
            list_l.append(s)
            list_n.append(n)
    l_r = min(list_l)
    n_r = list_n[list_l.index(l_r)]
    return (n_r, l_r)
        



"""""
===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   
                                                                                                              ПОДГОТОВКА
===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   
"""""



(processed, dict_rooms) = uncoder() # создание словарей маршрутов и комнат



# =============== ================ КНОПКИ И ФОН ================ ===============
button_start = Button(PNG(0,0, 100,50, 'от.png', 'от')) # пункт начала маршрута
button_end = Button(PNG(150,0, 100,50, 'до.png', 'до')) # пункт конца маршрута
button_through = Button(PNG(300,0, 536,50, 'через.png', 'через')) # промежутки
button_list = [button_start, button_end, button_through] # список кнопок
f1 = PNG(0,0, 1536,720, 'карта.png', 'map') # этаж 1
f1.draw() # рисуем фон
button_start.draw() #    
button_end.draw() #          
button_through.draw() #   
pygame.display.update() # обновляем моник
# =============== ==== =============== ==== =============== ==== ===============



# ===== ВСПОМОГАТЕЛЬНЫЕ ДАННЫЕ =====
run = True # работа
OT = False # меняем маршрут начала
DO = False # меняем маршрут конца
CH = False # меняем промежутки
text_1 = '' # пункт начала маршрута
r1 = ''
text_2 = '' # пункт конца маршрута
r2 = ''
text_3 = '' # промежутки
r3 = ''
draw_fact = False # рисовашка дороги
stage_1 = True #
stage_2 = False #
stage_3 = False #
stage_4 = False #
# =========== ========== ===========



"""""
===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   
                                                                                                             ОСНОВНОЙ КОД
===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   ===============   
"""""

z = 0
d2 = datetime.datetime.today()
print(d2 - d1)

while run:
    for i in pygame.event.get(): # проверка нажатия клавишь
        if i.type == pygame.QUIT: 
            sys.exit() 
        if i.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = i.pos
            mouse = [mouse_x, mouse_y]
            if i.button == 1:
                selected = button_select(button_list, mouse)
                if selected != 'no':
                    if selected.name == 'от':
                        OT = True
                        DO = False
                        CH = False
                    elif selected.name == 'до':
                        OT = False
                        DO = True
                        CH = False
                    elif selected.name == 'через':
                        OT = False
                        DO = False
                        CH = True
            elif i.button == 3:
                OT = False
                DO = False
                CH = False
            elif i.button == 2:
                if (r1 != 'туалет') and (r2 != 'туалет'):
                    if (r1 != 'лестница') and (r2 != 'лестница'):
                        if len(r3) > 1: (Li, le) = from_to(r1, r2, list(map(str, r3.split(', '))))
                        else: (Li, le) = from_to(r1, r2, [])
                    else:
                        if r1 == 'лестница': (Li, le) = toilet(r2, False)
                        else: (Li, le) = toilet(r1, False)
                else:
                    if r1 == 'туалет': (Li, le) = toilet(r2, True)
                    else: (Li, le) = toilet(r1, True)

                road = list(map(str, Li.split('_')))
                draw_fact = True
    if OT or DO or CH:
        keys = pygame.key.get_pressed()
        r = returner()
        if r != None:
            if OT:
                if r != 'enter':
                    if r != 'delet': text_1 += r
                    else: text_1 = text_1[0:-1]
                else: OT = False
            elif DO:
                if r != 'enter':
                    if r != 'delet': text_2 += r
                    else: text_2 = text_2[0:-1]
                else: DO = False
            elif CH:
                if r != 'enter':
                    if r != 'delet': text_3 += r
                    else: text_3 = text_3[0:-1]
                else: CH = False
    text1 = stile.render(text_1, True, (0,0,0))
    text2 = stile.render(text_2, True, (0,0,0))
    text3 = stile.render(text_3, True, (0,0,0))
    window.blit(text1, (30,15))
    window.blit(text2, (180,15))
    window.blit(text3, (370,15))

    for t_0000 in dict_rooms:
        pygame.draw.circle(window, (100,0,0), (dict_rooms[t_0000].x, dict_rooms[t_0000].y), 3)
 
    if draw_fact:
        for t_0001 in range(1, len(road)):
            route(road[t_0001-1], road[t_0001]).draw()
            
    if len(text_1) > 0:
        r1 = text_1
    if len(text_2) > 0:
        r2 = text_2
    r3 = text_3
    
    pygame.display.update() # обновляем моник
    window.fill( (255, 255, 255) ) # рисуем окошко
    pygame.time.delay(150)
    f1.draw()
    button_start.draw()
    button_end.draw()
    button_through.draw()


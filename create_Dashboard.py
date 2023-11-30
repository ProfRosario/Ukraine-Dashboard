import yaml
import datetime

# updated 3/31/23 Added Calendar to code
# updated 3/30/23 Added datetime to code
# Updated 4/04/23 Added an alt path when no title is included.
# Updated 4/04/23 Updated Exception error message.
# Updated 5/20/23 Added configTable for table, div and body.
# Updated 7/17/23 Added line break after image title.
# Updated 11/14/23 Improve stability to open/read a YAML file. Check if Keys exists. Removed useless commented code. Add default table, image & font setting. Add the flexibily to create a new target
# Updated 11/29/23 Added div-style to command properties.
# ToDo 11/29/23 Need to correct noimagefound check.
# Update 11/29/2023 Corrected default target tab.

# with open("config.yaml") as file:
#     try:
#         data = yaml.safe_load(file)
#         print(type(data))
#         print(data)

#     except yaml.YAMLError as exception:
#         print(exception)

debug = False
html_string =''
html_title =''
body = ''
css_file = ''
style = ''
target = '''target = "_blank"''' 


enable_new_tab = False
max_columns = 4
is_table_set = False
is_div_set = False
is_tr_set = False
is_td_set = False

count = 0
count_ID = 0
count_P = 0
count_Div = 0
count_Img = 0
count_Table = 0

# Default settings. All setting can be changed using the YAML file.
default_table_style = 'table-layout: fixed; width: 70% ; margin: 0 auto; border:0px solid rgb(0, 0, 0); border-radius: 20px; background-color:transparent; border-color: blue;'
default_tr_style = ' height: 60px; '
default_th_style = ' border: 4px solid black; text-align: center;align-items: center; align-self: center; width: 65%;'
default_td_style = ' font-size: 18px; text-align:center; border:0px solid rgb(0, 0, 0); border-radius: 10px; padding: 5px; border-style:solid; border-color: blue; background-color:transparent; '
default_div_style = ' background-color: rgb(255, 222, 173); '
default_body_style ='background-color: rgb(255, 222, 173);'
default_image_style = 'width: 70%; height: 75px; box-shadow: 0px 0px 20px #888; border-radius: 15px;'
default_para_style =  'margin: 5px 0px 0px; font-size: 14px; font-family: sans-serif ; text-align: center; font-weight: normal ; font-style: italic; color: blue;'

default_image_style_Header = 'width: 65%; height: 180px; display: block; margin-left: auto; margin-right: auto; box-shadow: 0px 0px 20px lightblue; border-radius:15px; border-style:dashed; border-color:black; border-width:3px;'

default_para_style_addTitle = 'margin: 20px 0px 0px; font-size: 28px; font-family: sans-serif ; text-align: center; font-weight: bold; font-style: normal; color: black; border:1px solid rgb(0, 0, 0); border-radius: 10px; border-color: blue; background-color:yellow; height: 40px; margin-left: auto; margin-right: auto; vertical-align:middle; width:65%;'

default_para_style_ReturnLink = 'margin: 5px 0px 0px; font-size: 14px; font-family: Times New Roman; text-align: center; font-weight: normal; font-style: italic; color: black; border: 0px solid rgb(0, 0, 0); border-radius: 10px; border-color: green; background-color:transparent; ; margin-left: auto; margin-right: auto; vertical-align:middle; width:25%; height: auto;'

default_para_style_addItem =  'font-size: 14px; font-family: sans-serif; font-weight: normal; font-style: italic; color: blue; margin: 0px 0px 0px; text-align: center;'

default_image_style_addItem = 'width: 70%; height: 75px; box-shadow: 2px 2px 20px gray; border-radius: 15px; border: 0px solid black;'

default_para_style_TimeStamp = 'margin: 5px 0px 0px; font-size: 14px; font-family: sans-serif ; text-align: center; font-weight: normal ; font-style: italic; color: blue;'


def reset_count():
  global count
  count = 0

def set_tr():
  global is_tr_set
  is_tr_set = True

def set_table():
  global is_table_set
  is_table_set = True

def set_div():
  global is_div_set
  is_div_set = True

def reset_tr():
  global is_tr_set
  is_tr_set = False

def reset_table():
  global is_table_set
  is_table_set = False

def reset_div():
  global is_div_set
  is_div_set = False

is_calendar_enabled = False

# file = open("style.css", "r")
# style = file.read()
# file.close()
# html_title ='evo-calendar'
# header =''
# body =''

calendar_css_link = '''
    <!-- // evo-calendar.css, followed by [theme-name].css (optional) -->
    <link rel="stylesheet" type="text/css" href="css/evo-calendar.css" />
    <link rel="stylesheet" type="text/css" href="css/evo-calendar.midnight-blue.css" />
'''
calendar_jquery = '''
    <!-- // evo-calendar.js, right after jQuery (required) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="js/evo-calendar.js"></script>
'''


f = open('config.yaml', 'r')
try:
    data = yaml.safe_load(f.read())
#    for id in data:
#          print('command = ', data[id]['command'])

except yaml.YAMLError as exception:

  print('======> Oops, error opening or reading YAML file \n')
  print('exception error code = ', exception)
# f.close()

# javascript = '''
#     <!-- // evo-calendar.js, right after jQuery (required) -->
#     <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
#     <script src="js/evo-calendar.js"></script>
# '''
javascript = ''


count = 0

# f2 = open('config.yaml', 'r')
# data = yaml.safe_load(f2.read())
# print('body = ' + body)

for id in data:
#----------------- configTable -----------------------------------
    if data[id]['command'] == 'configTable':
      if "table-style" in data[id]:
        table_style = data[id]['table-style']
      if "th-style" in data[id]:
        th_style = data[id]['th-style']
      if "tr-style" in data[id]:
        tr_style = data[id]['tr-style']
      if "td-style" in data[id]:
        td_style = data[id]['td-style']
      if "div-style" in data[id]:
        div_style = data[id]['div-style']
      if "body-style" in data[id]:
        body_style = data[id]['body-style']
        
      if "debug" in data[id]:
        debug = data[id]['debug']
        print("Command = " + data[id]['command'])
      else:
        debug = False
        
      style += '''
      .table_ID { ''' + default_table_style + '''}
      .th_ID { ''' + default_th_style + '''}
      .tr_ID { ''' + default_tr_style + '''}
      .td_ID { ''' + default_td_style + '''}
      .div_ID { ''' + default_div_style + '''}
      .body_ID { ''' + default_body_style + '''}
      .para_ID { ''' + default_para_style + '''}
      '''

# ---------------- addHeaderImage --------------------------------
    elif data[id]['command'] == 'addHeaderImage':
      if debug:
        print("Command = " + data[id]['command'])

      if "image-style" in data[id]:
        img_style = data[id]['image-style']
      else:
        img_style= default_image_style_Header
      if "title" in data[id]:
        title = data[id]['title']
      else:
        title = ''
      if "image" in data[id]:
        image = data[id]['image']
      else:
        image = 'noimagefound.png'

      if "div-style" in data[id]:
         div_style = data[id]['div-style']
      else:
         div_style = div_style

      count_Div = count_Div + 1
      div_ID = 'div_ID' + str(count_Div)
      
      count_Img = count_Img + 1
      img_ID = 'img_ID' + str(count_Img)
      
      style += '''
      .''' + img_ID + ''' { ''' + img_style + '''}
      .''' + div_ID + ''' { ''' + div_style + '''}
      '''

      html_title = title
      body += '''
    <div class=" ''' + div_ID + '''">
      <img src="''' + image + '''" alt="''' + title + '''" class ="''' + img_ID + '''">
    </div>
  '''
# ---------------- addStyle --------------------------------
    elif data[id]['command'] == 'addStyle':
      if debug:
        print("Command = " + data[id]['command'])

      if "css_file" in data[id]:
        file = open(data[id]['css_file'], "r")
        style = file.read()
        file.close()

# ---------- enableNewTab ------This is not being used ----------

    elif data[id]['command'] == 'enableNewTab':
      if debug:
        print("Command = " + data[id]['command'])
      if 'enable_new_tab' in data[id]:
        target = '''target = "_blank"'''

#---------------- addReturnLink ------------------------
    elif data[id]['command'] == 'addReturnLink':
      if debug:
        print("Command = " + data[id]['command'])

      if 'title' in data[id]:
        title = data[id]['title']
      else:
        title = " "     
      if  data[id]['link']:
        link =  data[id]['link']
      else:
        link = 'https:/www.google.com/'
      if 'font-style' in data[id]:
        p_style = data[id]['font-style']
      else:
        p_style = default_para_style_ReturnLink
# ? Is this needed here ?
      if 'enable_new_tab' in data[id]:
        if data[id]['enable_new_tab'] == True:
          target = '''target = "_blank"'''
        else:
          target = '''target = " "''' 

      if "div-style" in data[id]:
         div_style = data[id]['div-style']
      else:
         div_style = default_div_style


      #created = datetime.datetime.now()
      
      if is_table_set:
        # is_table_set = False
        reset_table()
# add body parts
        body += '''
      </table>'''
      if is_div_set:
        # is_div_set = False
        reset_div()
        body += '''
    </div>'''
      count_Div = count_Div + 1
      div_ID = 'div_ID' + str(count_Div)

      count_P = count_P + 1
      para_ID = 'para_ID' + str(count_P)
# add style parts
      style += '''
      .''' + para_ID + ''' { ''' + p_style + '''}
      .''' + div_ID + ''' { ''' + div_style + '''}
      '''
# add body parts
      body += '''
    <!-- addReturnLink -->
    <div class="'''+ div_ID + '''">
        <p class = "''' + para_ID + '''"><a href="''' + link + '''">''' + title + '''</a></p>
    </div>
    '''   
      reset_count()  # count is set to zero

#------addTimeStamp
    elif data[id]['command'] == 'addTimeStamp':
      if debug:
        print("Command = " + data[id]['command'])

      if "font-style" in data[id]:
        p_style = data[id]['font-style']
      else:
        p_style = default_para_style_TimeStamp
      if "title" in data[id]:
        title = data[id]['title']
      else:
        title = 'This page was created on: '
      if "div-style" in data[id]:
         div_style = data[id]['div-style']
      else:
         div_style = default_div_style
      
      x = datetime.datetime.now()
      if is_table_set:
        # is_table_set = False
        reset_table()
# add body parts
        body += '''
      </table>'''
        
      if is_div_set:
        # is_div_set = False
        reset_div()
# add body parts
        body += '''
    </div>'''
      count_Div = count_Div + 1
      div_ID = 'div_ID' + str(count_Div)

      count_P = count_P + 1
      para_ID = 'para_ID' + str(count_P)
# add style parts    
      style += '''
      .''' + para_ID + ''' { ''' + p_style + '''}
      .''' + div_ID + ''' { ''' + div_style + '''}
      '''

      # date = x.strftime("%A") + ' ' + x.strftime("%B") + ' ' + x.strftime("%C") + ' ' + str(x.year) +' --- ' + x.strftime("%c")
      dateCreated = x.strftime("%m/%d/%Y, @ %H:%M hrs")
# add body parts
      body += '''
    <!-- addTimeStamp -->
    <div class="''' + div_ID + ''' ">
        <p class = "''' + para_ID + ''' ">''' + title + dateCreated + '''</p>
    </div>'''
      reset_count()  # count is set to zero

# -------------------addTitle------
    elif data[id]['command'] == 'addTitle':
      if debug:
        print("Command = " + data[id]['command'])

      if 'title' in data[id]:
        title =  data[id]['title']
      else:
        title = ' ' 
      if 'font-style' in data[id]:
        p_style = data[id]['font-style']
      else:
        p_style = default_para_style_addTitle
      if "div-style" in data[id]:
         div_style = data[id]['div-style']
      else:
         div_style = default_div_style

      if is_tr_set:
        # is_tr_set = False
        reset_tr()
# add body parts
        body += '''
       </tr>'''

      if is_table_set:
        # is_table_set = False
        reset_table()
# add body parts
        body += '''
      </table>'''
        
      if is_div_set:
        # is_div_set = False
        reset_div()
# add body parts
        body += '''
    </div>
    '''
      count_Div = count_Div + 1
      div_ID = 'div_ID' + str(count_Div)

      count_P = count_P + 1
      para_ID = 'para_ID' + str(count_P)

# add style parts
 
      style += '''
      .''' + para_ID + ''' { ''' + p_style + '''}
      .''' + div_ID + ''' { ''' + div_style + '''}
      '''

# add body parts
      body += '''      
    <!-- addTitle -->
    <div class="''' + div_ID + '''">
      <p class = " ''' + para_ID + ''' ">''' + data[id]['title'] + '''</p>  
    </div>
    '''
      reset_count()  # count is set to zero

#------------- Set Max Columns ----------------------
    elif data[id]['command'] == 'setMaxColumns':
      if debug:
        print("Command = " + data[id]['command'] + ", max_columns = " + str(max_columns))
        # print("Command = ", data[id]['command'] , ", max_columns = ", max_columns)

      if 'max_columns' in data[id]:
        max_columns = data[id]['max_columns']

      if is_table_set:
        # is_table_set = False
        reset_table()
# add body parts
        body += '''
      </table>'''

      if is_div_set:
        # is_div_set = False
        reset_div()
# add body parts
        body += '''
    </div>
    '''
      reset_count()  # count is set to zero

#-------------------- addItem --------------------------------- 
    elif data[id]['command'] == 'addItem':
      if debug:
        print("Command = " + data[id]['command'])

      if "title" in data[id]:
        title = data[id]['title']
      else:
        title = ''
      if "font-style" in data[id]:
        p_style = data[id]['font-style']
      else:
        p_style = default_para_style_addItem
      if "image-style" in data[id]:
        img_style = data[id]['image-style']
      else:
        img_style = default_image_style_addItem

      if ("image" in data[id] and "image-style" in data[id]):
        image = data[id]['image']
      else:
        image = 'noimagefound.png'
      if "link" in data[id]:
        link = data[id]['link']
      else:
        link = 'https://www.google.com'
        title = "Google"
      if "target" in data[id]:
        target = '''target = "'''  + data[id]['target'] + '''"'''
      if "div-style" in data[id]:
         div_style = data[id]['div-style']
      else:
         div_style = default_div_style
                   

      if not is_div_set:
        # is_div_set = True
        set_div()
# add body parts   
        count_Div = count_Div + 1
        div_ID = 'div_ID' + str(count_Div)
        body += '''
    <div class="'''+ div_ID + ''' ">'''
        style += '''
      .''' + div_ID + ''' { ''' + div_style + '''}'''
        
      if not is_table_set:
        # is_table_set = True
        set_table()
# add body parts
        body += '''
      <table class="table_ID">'''
      
      if (count == 0) or ( not is_tr_set) :
        # is_tr_set = True
        set_tr()
# add body parts
        body += '''
        <tr class="tr_ID">'''
      
      count_P = count_P + 1
      para_ID = 'para_ID' + str(count_P)

# add style parts
      style += '''
      .''' + para_ID + ''' { ''' + p_style + '''}
      .''' + div_ID + ''' { ''' + div_style + '''}
      ''' 
      count_Img = count_Img + 1
      img_ID = 'img_ID' + str(count_Img)

# add style parts    
      style += '''
      .''' + img_ID + ''' { ''' + img_style + '''}
      '''

      if title == '' or title == 'None':
        alt_title = link
        title = ' '
      else:
        alt_title = title
# add body parts
      body += '''
          <!-- addItems -->
          <td class="td_ID">
            <p class = "''' + para_ID + '''"><a href="''' + link + '''" ''' + target + '''>''' + title + '''<br> <img src="''' + image + '''" alt="''' + alt_title + ''' "
               class = "''' + img_ID + '''"></a></p>
          </td>'''

      count = count + 1
      # print('====== > Max count = ', max_columns)
      # print('=======>Count = ', count)
      if count == max_columns:
        # is_tr_set = False
        reset_tr()
# add body parts
        body += '''
        </tr>''' 
        reset_count()

#------------------ addToDo -----------------------------
    elif data[id]['command'] == 'addToDo':
      if debug:
        print("Command = " + data[id]['command'])

      if 'font-style' in data[id]:
          p_style = data[id]['font-style']
      if 'title' in data[id]:
        title = data[id]['title']
      else:
        title = "no title"
      if 'date_start' in data[id]:
        date_start = data[id]['date_start']
      else:
        date_start = ""
      if 'date_end' in data[id]:
        data_end = data[id]['date_end']
      else:
        date_end = ""
      if 'complete' in data[id]:
          complete = data[id]['complete']
      else:
          complete = "no"

      if not is_div_set:
        # is_div_set = True
        set_div()
# add body parts
        body += '''
    <div class="div_ID">'''

      if not is_table_set:
        # is_table_set = True
        set_table()
# add body parts
        body += '''
      <table class="table_ID">'''
      
      if (count == 0) or ( not is_tr_set) :
       # is_tr_set = True
        set_tr()
# add body parts
        body += '''
        <tr class="tr_ID">'''
      
      if complete== 'yes' or complete == 'Yes':
        p_style = "text-decoration:line-through; " + default_para_style
      else:
        p_style = default_para_style

      count_P = count_P + 1
      para_ID = 'para_ID' + str(count_P)
# add style parts
      style += '''
      .''' + para_ID + ''' { ''' + p_style + '''}
      '''
      # print('style = ', style)
# add body parts  
      body += '''
          <td class="td_ID">
            <p class = "''' + para_ID + '''">''' + title + '''</p>
            <p></p>
            <p class = "''' + para_ID + '''">Start date: ''' + date_start + '''</p>
            <p class = "''' + para_ID + '''">End date: ''' + date_end + '''</p>
          </td>'''
      count = count + 1

      # print('=======>Count = ', count)
      if count == max_columns:
        # is_tr_set = False
        reset_tr()
# add body parts 
        body += '''
        </tr>'''
        reset_count()

#-------------- Add Calendar Events

    elif  data[id]['command'] == "addEvent":
      if debug:
        print("Command = " + data[id]['command'])

        if is_table_set:
        # is_table_set = False
            reset_table()
            body += '''
      </table>'''
        if is_div_set:
            # is_div_set = False
            reset_div()
            body += '''
    </div>
        '''
        is_calendar_enabled = True;
        if count == 0:
            count +=1
            body +='''
    <!-- // this is where your calendar goes.. :) -->
    <div id="calendar"></div>
    '''
            javascript += '''
        <script>
            // initialize your calendar, once the page's DOM is ready
            var myEventList = [];
            '''

        if count > 0:
            # print('==============>count = ' + str(count))
            count +=1

            javascript +=   '''
                myEventList.push(
                {
                    id: "''' + id + '''",
                    name:"''' + data[id]['name'] +'''",
                    badge:  "''' + data[id]['badge'] +'''",
                    date:"''' + data[id]['date'] +'''",
                    description: "''' + data[id]['description'] + '''",
                    type: "''' + data[id]['type'] +'''",
                    color: "''' + data[id]['color'] +'''",
                    everyYear: ''' + data[id]['everyYear'] +''',
                });'''
if is_calendar_enabled:
    javascript = calendar_jquery + javascript + '''
            // initialize your calendar, once the page's DOM is ready
            $(document).ready(
                function () {
                    $('#calendar').evoCalendar(
                    {
                        // settingName: settingValue
                        'todayHighlight': false,
                        calendarEvents: myEventList
                    })
            })
        </script> '''
    
if not is_calendar_enabled:
  calendar_css_link = ''
  javascript = ''

# Create an index.html file
html_string = '''
<!DOCTYPE html>
<html>
  <head>
     <title>''' + html_title + '''</title>
    ''' + calendar_css_link + '''
     <style>
     ''' + style + '''
     </style>
  </head>
  <body class = "body_ID">
    ''' + body + '''
  ''' + javascript + '''
  </body>
</html>'''

if debug:
    print(html_string)

f = open("index.html","w" )
f.write(html_string)

f.close()
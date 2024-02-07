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
# Updated 12/7/2023 Added the command AddImageMap
# Updated 12/8/2023 Add div_style in AddImageMap command.
# Corrected error in default global setting with ConfigTable Command
# Updated 12/10/23 Corrected tags, <tr> and <table> & <div>, closing logic errors within code. 
# Updated 12/11/2023 Added anchor link to header Image
# Update 12/12/23 Clean and organized code to make it more readable and reliable. Corrected calendar error.  Corrected error on todo list command.
# Update 12/12/23 Updated addEvent command - corrected code & indentation error error and added div-style
# Updated 12/14/23 Organized code to make it more efficient, readable and maintainable. Remove old comments and spaces.
# Updated 12/14/23 Added alt_title to <src> tag.
# Updated 1/19/24 Added addLink command. Added <link> tag in header section of HTML.
# * Todo Updated 1/19/24 Added addScipt command. 
# * Todo Updated 1/19/24 Added <script> tab in header section
# Updated 1/20/24 Corrected issue with href Target property. Removed enableNewTab command and code.  *All YAML files needs to be updated too.
# Updated 1/20/24 Change variable names image-style to img-style and font-style to p-style. YAML file needs to be updated too.
# Updated 1/20/24 Added 'Target' property to addReturnLink.
# Updated 1/20/24 Corrected issues with 'alt= alt_title' string
# Updated 1/20/24 Changed the global default Target property to "_blank"
# Updated 1/21/24 Removed javascript from code. Add new commonds AddScript, AddJava, AddLink, AddMeta and AddStyle.
# Updated 1/21/24 Added 'html-title' property to addConfig command
# Updated 1/28/24 
#   - Renamed function close_opened_tr_table_div_tags() to close_all_tags(). 
#   - Renamed all variables with 'dash' to 'underscore' example img-style to img_style, div-style to div_style, p-style to p_style ... etc. 
#        **** These variable changes will require an update to all the YAML files
# Updated 1/29/24 
#  - Fixed the following commands: AddImageMap & AddJavascript. Added the following new commands addScriptXML, AddLinkXML and AddMetaXML to read external files. 
#  - Removed the following commands Script, AddLink, AddMeta
#  - Clean code: Replaced count = count + 1 with count += 1, removed code with format = [".jpg",".png",".jpeg","JPG", "PNG", "JPEG"], corrected global issues with 'count' with addItem and addEvent
#  - Added 'target' attribute to all hrefs
#  - Added external css file to control hyperlink color.

debug = False
html_string =''
html_title =''
body = ''
css_file = ''
style = ''
script = ''

add_link = ''
add_meta = ''
add_java = ''
add_css = ''
add_header = ''
add_footer = ''
add_script =''
add_Image_Map =''

max_columns = 4
is_table_set = False
is_div_set = False
is_tr_set = False
is_td_set = False

# count = 0
count_ToDo_Column = 0
count_Column = 0
count_Event = 0
count_ID = 0
count_P = 0
count_Div = 0
count_Img = 0
count_Table = 0
# date_end = ''
# date_start = ''

# Default settings. All setting can be changed using the YAML file.
default_table_style = 'table-layout: fixed; width: 70% ; margin: 0 auto; border:0px solid rgb(0, 0, 0); border-radius: 20px; background-color:transparent; border-color: blue;'
default_tr_style = 'height: 60px; '
default_th_style = 'border: 4px solid black; text-align: center;align-items: center; align-self: center; width: 65%;'
default_td_style = 'font-size: 18px; text-align:center; border:0px solid rgb(0, 0, 0); border-radius: 10px; padding: 5px; border-style:solid; border-color: blue; background-color:transparent;'
default_div_style = 'background-color: rgb(255, 222, 173);'
default_body_style = 'background-color: rgb(255, 222, 173);'
default_img_style = 'width: 70%; height: 75px; box-shadow: 0px 0px 20px #888; border-radius: 15px;'
default_p_style =  'margin: 5px 0px 0px; font-size: 14px; font-family: sans-serif ; text-align: center; font-weight: normal ; font-style: italic; color: blue;'

default_img_style_Header = 'width: 65%; height: 180px; display: block; margin-left: auto; margin-right: auto; box-shadow: 0px 0px 20px lightblue; border-radius:15px; border-style:dashed; border-color:black; border-width:3px;'

default_p_style_addTitle = 'margin: 20px 0px 0px; font-size: 28px; font-family: sans-serif ; text-align: center; font-weight: bold; font-style: normal; color: black; border:1px solid rgb(0, 0, 0); border-radius: 10px; border-color: blue; background-color:yellow; height: 40px; margin-left: auto; margin-right: auto; vertical-align:middle; width:65%;'

default_p_style_ReturnLink = 'margin: 5px 0px 0px; font-size: 14px; font-family: Times New Roman; text-align: center; font-weight: normal; font-style: italic; color: black; border: 0px solid rgb(0, 0, 0); border-radius: 10px; border-color: green; background-color:transparent; ; margin-left: auto; margin-right: auto; vertical-align:middle; width:25%; height: auto;'

default_p_style_addItem =  'font-size: 14px; font-family: sans-serif; font-weight: normal; font-style: italic; color: blue; margin: 0px 0px 0px; text-align: center;'

default_img_style_addItem = 'width: 70%; height: 75px; box-shadow: 2px 2px 20px gray; border-radius: 15px; border: 0px solid black;'

default_p_style_TimeStamp = 'margin: 5px 0px 0px; font-size: 14px; font-family: sans-serif ; text-align: center; font-weight: normal ; font-style: italic; color: blue;'

default_target = "_blank"


def reset_count():
  global count_Column
  global count_ToDo_Column
  count_Column = 0
  count_ToDo_Column = 0

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

def close_all_tags():
  # Checks and closes any previously opened <tr>, <table> and <div> start tags before creating a new div tag.
  global body
  if is_tr_set:
    reset_tr()
    body += '''
        </tr>'''     
  if is_table_set:
    reset_table()
    body += '''
      </table>'''
  if is_div_set:
    reset_div()
    body += '''
    </div>
    '''
  reset_count()  # count is set to zero

is_calendar_enabled = False

def enable_calendar():
  global is_calendar_enabled
  is_calendar_enabled = True

def disable_calendar():
  global is_calendar_enabled
  is_calendar_enabled = False


f = open('config.yaml', 'r')
try:
    data = yaml.safe_load(f.read())
#    for id in data:
#          print('command = ', data[id]['command'])

except yaml.YAMLError as exception:

  print('======> Oops, error opening or reading YAML file \n')
  print('exception error code = ', exception)
f.close()


for id in data:

#------------------- Command configTable --------------------------
    if data[id]['command'] == 'configTable':

      close_all_tags()

      if 'html_title' in data[id]: html_title = data[id]['html_title']

      if 'table_style' in data[id]: default_table_style = data[id]['table_style']

      if 'th_style' in data[id]: default_th_style = data[id]['th_style']

      if 'tr_style' in data[id]: default_tr_style = data[id]['tr_style']

      if 'td_style' in data[id]: default_td_style = data[id]['td_style']

      if 'div_style' in data[id]: default_div_style = data[id]['div_style']

      if 'body_style' in data[id]: default_body_style = data[id]['body_style']

      if 'p_style' in data[id]: default_p_style = data[id]['p_style']

      if 'target' in data[id] : default_target = data[id]['target']

      if 'debug' in data[id]: debug = data[id]['debug']

      if debug : print("Command = " + data[id]['command'])
       
      style += '''
      .body_ID { ''' + default_body_style + '''}
      .div_ID { ''' + default_div_style + '''}
      .table_ID { ''' + default_table_style + '''}
      .tr_ID { ''' + default_tr_style + '''}
      .th_ID { ''' + default_th_style + '''}
      .td_ID { ''' + default_td_style + '''}
      .p_ID { ''' + default_p_style + '''}
      '''

# ------------------ Command addHeaderImage -----------------------
    elif data[id]['command'] == 'addHeaderImage':
      
      close_all_tags()
      title = 'No Default Image Found'
      alt_title = "No Default Image Found" 
      image = './images/noimagefound.png'
      link = ''
      img_style = default_img_style_addItem
      p_style = default_p_style_addItem
      div_style = default_div_style
      target = default_target
      
      if debug: print("Command = " + data[id]['command'])    
        
      if 'title' in data[id]: title = data[id]['title']

      if 'image' in data[id]:
        image = data[id]['image']
        if len(image) < 5:
          alt_title = image
          image = './images/noimagefound.png'

      if 'link' in data[id]: link = data[id]['link']
      
      if 'img_style' in data[id]: img_style = data[id]['img_style']      

      if 'div_style' in data[id]: div_style = data[id]['div_style']

      if 'target' in data[id]: target = data[id]['target']

      count_Div += 1
      div_ID = 'div_ID' + str(count_Div)

      count_Img += 1
      img_ID = 'img_ID' + str(count_Img)

      style += '''
      .''' + div_ID + ''' { ''' + div_style + '''}
      .''' + img_ID + ''' { ''' + img_style + '''}
      '''
      alt_title = title
   
      body += '''
    <!-- addHeaderImage -->
    <div class = " ''' + div_ID + '''">
      <a href = "''' + link + '''" target = "''' + target + '''"><img src = "''' + image + '''" alt = "''' + alt_title + '''" class ="''' + img_ID + '''"></a>
    </div>
    '''
        
# ------------------ Command addStyle ----------------------- -----
    elif data[id]['command'] == 'addStyle':
      
      if debug: print("Command = " + data[id]['command'])
      
      if 'style' in data[id]:
        css_style = data[id]['style']
        add_css += '''
    <style> 
        ''' + css_style + '''
    </style>'''
      
      if 'file_name' in data[id]:
        file_name = data[id]['file_name']
        file = open(file_name, "r")
        add_css += '''
    <style> 
        ''' + file.read() + '''
    </style>'''
        file.close()

# ---------------- addScript ---- ------------
    elif data[id]['command'] == 'addScriptXML':

      if debug: print("Command = " + data[id]['command'])
      
      if 'script' in data[id]:
        script = data[id]['script']
        add_script += ''' 
        ''' + script + '''
        '''

      if 'file_name' in data[id]:
        file_name = data[id]['file_name']
        file = open(file_name, "r")
        add_script += ''' 
        ''' + file.read() + '''
        '''
        file.close()
      
# ---------------- addLink ----------------
    elif data[id]['command'] == 'addLinkXML':
      
      if debug: print("Command = " + data[id]['command'])
      
      if 'link' in data[id]:
        link = data[id]['link']
        add_link += ''' 
        ''' + link + '''
        '''

      if 'file_name' in data[id]:
        file_name = data[id]['file_name']
        file = open(file_name, "r")
        add_link += ''' 
        ''' + file.read() + '''
        '''
        file.close()
               
#---------------------Command addMeta data ------------------------  
    elif data[id]['command'] == 'addMetaXML':
      
      if debug: print("Command = " + data[id]['command'])
      
      if 'meta' in data[id]:
        meta = data[id]['meta']
        add_meta += ''' 
        ''' + meta + '''
        '''

      if 'file_name' in data[id]:
        file_name = data[id]['file_name']
        file = open(file_name, "r")
        add_meta += ''' 
        ''' + file.read() + '''
        '''
        file.close()
  
#---------------------Command addJavaScript -----------------------
    elif data[id]['command'] == 'addJavascript':

      if debug: print("Command = " + data[id]['command'])
      
      if 'script' in data[id]:
        javascript = data[id]['script']
        add_java += '''
    <script> 
        ''' + javascript+ '''
    </script>'''

      if 'file_name' in data[id]:
        file_name = data[id]['file_name']
        file = open(file_name, "r")
        add_java += '''
    <script> 
        ''' + file.read() + '''
    </script>'''
        file.close()

#---------------------Command addReturnLink -----------------------
    elif data[id]['command'] == 'addReturnLink':     
      
      close_all_tags() 
     
      title = ''
      link = ' '
      p_style = default_p_style_ReturnLink
      div_style = default_div_style
      image = './images/noimagefound.png'
      target = default_target

      if debug: print("Command = " + data[id]['command'])

      if 'title' in data[id]: title = data[id]['title']
        
      if 'link' in data[id]: link =  data[id]['link']

      if 'p_style' in data[id]: p_style = data[id]['p_style']

      if 'target' in data[id]: target = data[id]['target']

      if 'div_style' in data[id]: div_style = data[id]['div_style']
      
      count_Div += 1
      div_ID = 'div_ID' + str(count_Div)

      count_P += 1
      p_ID = 'p_ID' + str(count_P)

      style += '''
      .''' + div_ID + ''' { ''' + div_style + '''}
      .''' + p_ID + ''' { ''' + p_style + '''}
      '''

      body += '''
    <!-- addReturnLink -->
    <div class = "'''+ div_ID + '''">
        <p class = "''' + p_ID + '''"><a href = "''' + link + '''" target = "''' + target + '''">''' + title + '''</a></p>
    </div>
    '''   
     
# -------------------Command addTimeStamp -------------------------
    elif data[id]['command'] == 'addTimeStamp':
      
      close_all_tags()
      
      title = ''
      p_style = default_p_style_TimeStamp
      div_style = default_div_style

      if debug: print("Command = " + data[id]['command'])
      
      if 'title' in data[id]: title = data[id]['title']
      
      if 'p_style' in data[id]: p_style = data[id]['p_style']

      if 'div_style' in data[id]: div_style = data[id]['div_style']

      x = datetime.datetime.now()

      count_Div += 1
      div_ID = 'div_ID' + str(count_Div)

      count_P += 1
      p_ID = 'p_ID' + str(count_P)

      style += '''
      .''' + div_ID + ''' { ''' + div_style + '''}
      .''' + p_ID + ''' { ''' + p_style + '''}
      '''
      # date = x.strftime("%A") + ' ' + x.strftime("%B") + ' ' + x.strftime("%C") + ' ' + str(x.year) +' --- ' + x.strftime("%c")
      dateCreated = x.strftime("%m/%d/%Y, @ %H:%M hrs")

      body += '''
    <!-- addTimeStamp -->
    <div class = "''' + div_ID + ''' ">
        <p class = "''' + p_ID + ''' ">''' + title + dateCreated + '''</p>
    </div>
    '''

#------------------- Command addTitle------------
    elif data[id]['command'] == 'addTitle':
      
      close_all_tags()

      title = ''
      p_style = default_p_style_addTitle
      div_style = default_div_style
      
      if debug: print("Command = " + data[id]['command'])

      if 'title' in data[id]: title =  data[id]['title']
 
      if 'p_style' in data[id]: p_style = data[id]['p_style']
 
      if 'div_style' in data[id]: div_style = data[id]['div_style']

      count_Div += 1
      div_ID = 'div_ID' + str(count_Div)

      count_P += 1
      p_ID = 'p_ID' + str(count_P)

      style += '''
      .''' + div_ID + ''' { ''' + div_style + '''}
      .''' + p_ID + ''' { ''' + p_style + '''}
      '''

      body += '''      
    <!-- addTitle -->
    <div class = "''' + div_ID + '''">
      <p class = " ''' + p_ID + ''' ">''' + data[id]['title'] + '''</p>  
    </div>
    '''

#------------------- Command Set Max Columns ----------------------
    elif data[id]['command'] == 'setMaxColumns':
      
      close_all_tags()
      
      if 'max_columns' in data[id]: max_columns = data[id]['max_columns']
      
      if debug: print("Command = " + data[id]['command'] + ", max_columns = " + str(max_columns))

#--------------------Command addItem --------------------------------- 
    elif data[id]['command'] == 'addItem':
      
      title = ''
      alt_title = "No Default Image Found"
      p_style = default_p_style_addItem
      img_style = default_img_style_addItem
      link = ''
      div_style = default_div_style
      image = './images/noimagefound.png'
      target = default_target
      
      if debug: print("Command = " + data[id]['command'])  
      
      if 'title' in data[id]: title = data[id]['title']

      if 'image' in data[id]:
        image = data[id]['image']
        alt_title = image
        if len(image) < 5:
          alt_title = image
          image = './images/noimagefound.png'   
      
      if 'p_style' in data[id]: p_style = data[id]['p_style']
      
      if 'img_style' in data[id]: img_style = data[id]['img_style']
    
      if 'link' in data[id]: link = data[id]['link']
  
      if 'div_style' in data[id]: div_style = data[id]['div_style']

      if 'target' in data[id]: target = data[id]['target']
              
      if not is_div_set:
        set_div()  
        count_Div += 1
        div_ID = 'div_ID' + str(count_Div)
        
        style += '''
      .''' + div_ID + ''' { ''' + div_style + '''}'''
        
        body += '''
    <!-- addItems -->    
    <div class = "'''+ div_ID + ''' ">'''
              
      if not is_table_set:
        set_table()
        body += '''
      <table class = "table_ID">'''
      
      if (count_Column == 0) or ( not is_tr_set) :
        # is_tr_set = True
        set_tr()
        body += '''
        <tr class = "tr_ID">'''
   
      count_P += 1
      p_ID = 'p_ID' + str(count_P)

      count_Img += 1
      img_ID = 'img_ID' + str(count_Img)
##
      style += '''
      .''' + p_ID + ''' { ''' + p_style + '''}
      .'''  + img_ID + ''' { ''' + img_style + '''}
      '''
      body += '''
          <!-- addItems -->
          <td class = "td_ID">
            <p class = "''' + p_ID + '''"><a href = "''' + link + '''" target = "''' + target + '''">''' + title + '''<br><img src = "''' + image + '''" alt = "''' + alt_title + ''' "
               class = "''' + img_ID + '''"></a></p>
          </td>'''

      count_Column += 1

      if debug: print('=======>Count = ', count_Column)

      if count_Column == max_columns:
        reset_tr()
        reset_count()
        body += '''
        </tr>''' 

#------------------Command  addImageMap -------------------------
    elif data[id]['command'] == 'addImageMap':
      
      close_all_tags()
      
      title = 'No Image Found'
      alt_title = 'No Image Found'
      link = ''
      image = './images/noimagefound.png'
      img_style = default_img_style_addItem
      div_style = default_div_style

      if debug: print("Command = " + data[id]['command'])

      if 'title' in data[id]: title = data[id]['title']

      if 'image' in data[id]:
        image = data[id]['image']
        if len(image) < 5:
          alt_title = image
          image = './images/noimagefound.png'  

      if 'link' in data[id]: link = data[id]['link']  # TODO SHOULD REMOVE 1/29/24

      if 'use_map' in data[id]: use_map = data[id]['use_map']
      
      if 'map_style_html' in data[id]: add_Image_Map += data[id]['map_style_html']
      
      if 'file_name' in data[id]:
        file_name = data[id]['file_name']
        file = open(file_name, "r")
        add_Image_Map += file.read()
        file.close()

      if 'img_style' in data[id]: img_style = data[id]['img_style']

      if "div_style" in data[id]: div_style = data[id]['div_style']
 
      count_Div += 1
      div_ID = 'div_ID' + str(count_Div) 
      
      # add a new div_ID to the style list 
      style += '''
      .''' + div_ID + ''' { ''' + div_style + '''}'''  
      
      body += '''
    <!-- addImageMap -->
    <div class = "'''+ div_ID +'''">
      <br/>    
      <img src = "''' + image +  '''" alt = "''' + alt_title + ''' " usemap = "#''' + use_map + '''" style = " ''' + img_style + ''' ">
      <br/>
    </div>
    '''      

#------------------Command addToDo -----------------------------
    elif data[id]['command'] == 'addToDo':

      title = "no title"
      date_start = " "    
      date_end = " "
      complete = "no"
      div_style = default_div_style
      p_style = default_p_style

      if debug: print("Command = " + data[id]['command'])

      if 'title' in data[id]: title = data[id]['title']

      if 'date_start' in data[id]: date_start = data[id]['date_start']

      if 'date_end' in data[id]: date_end = data[id]['date_end']

      if 'complete' in data[id]: complete = data[id]['complete']

      if 'p_style' in data[id]: p_style = data[id]['p_style']

      if "div_style" in data[id]: div_style = data[id]['div_style']

      # Checks if any previous <div> and <table> tags were created. If not, a new <div> or/and <table> tags are created.
      if not is_div_set:
        set_div()
        count_Div += 1
        div_ID = 'div_ID' + str(count_Div)
        style += '''
      .''' + div_ID + ''' { ''' + div_style + '''}'''
        
        body += '''
    <!-- addToDo -->
    <div class = "'''+ div_ID + ''' ">'''

      if not is_table_set:
        set_table()
        body += '''
      <table class = "table_ID">'''
      
      if (count_ToDo_Column == 0) or ( not is_tr_set) :
        set_tr()
        body += '''
        <tr class = "tr_ID">'''
      
      if complete== 'yes' or complete == 'Yes': p_style = "text-decoration:line-through; " + p_style

      count_P += 1
      p_ID = 'p_ID' + str(count_P)

      style += '''
      .''' + p_ID + ''' { ''' + p_style + '''}
      '''
      body += '''
          <td class = "td_ID">
            <p class = "''' + p_ID + '''">''' + title + '''</p>
            <p></p>
            <p class = "''' + p_ID + '''">Start date: ''' + date_start + '''</p>
            <p class = "''' + p_ID + '''">End date: ''' + date_end + '''</p>
          </td>'''
      
      count_ToDo_Column += 1

      if debug: print('=======>Count Columns= ', count_Column)

      if count_ToDo_Column == max_columns:
        reset_tr()
        reset_count()
        body += '''
        </tr>'''

#------------------Command addEvent------------------------
#-----------------This code creates a calendar using jquery code and javascript    

    elif  data[id]['command'] == "addEvent":
      
      # close_all_tags()
      
      name = " "
      badge = " "
      date_ = " "
      description = " "
      type = " "
      color = " "
      everyYear = ""
      div_style = default_div_style

      if debug: print('Command = ' + data[id]['command'])

      if 'name' in data[id]: name = data[id]['name']

      if 'badge' in data[id]: badge = data[id]['badge']

      if 'date' in data[id]:  date_ = data[id]['date']
      
      if 'description' in data[id]: description = data[id]['description']

      if 'type' in data[id]: type = data[id]['type']

      if 'color' in data[id]: color = data[id]['color']

      if 'everyYear' in data[id]: everyYear = data[id]['everyYear']

      if 'div_style' in data[id]: div_style = data[id]['div_style']

      if not is_calendar_enabled: enable_calendar()
  # what is this doing 
      if count_Event == 0:
        count_Div += 1
        div_ID = 'div_ID' + str(count_Div)

        style += '''
      .''' + div_ID + ''' { ''' + div_style + '''}'''
        
        body +=''' 
    <!-- This is the location where the calendar will be inserted. -->
    <!-- addEvent Calendar -->
    <div class = " ''' + div_ID + '''"  id = "calendar"></div>
    '''
        
        script += '''
    <!-- initialize your calendar, once the page's DOM is ready -->
       var myEventList = [];
    '''

      count_Event += 1
      if debug: print('==============>count_Event = ' + str(count_Event))

      script +=   '''
                myEventList.push(
                {
                    id: "''' + id + '''",
                    name:"''' + name +'''",
                    badge:  "''' + badge +'''",
                    date:"''' + date_ +'''",
                    description: "''' + description + '''",
                    type: "''' + type +'''",
                    color: "''' + color +'''",
                    everyYear: ''' + everyYear +''',
                });'''

#---------------- END OF ALL COMMANDS ---------------------------------

# ------------------- Create an index.html file

html_string = '''
<!DOCTYPE html>
<html>
  <head>    
    <title>''' + html_title + '''</title>
     ''' + add_link + '''
     ''' + add_meta + '''
    <style>
     ''' + style + '''
    </style>
     ''' + add_css + '''
     ''' + add_script + '''
     ''' + add_java + '''
    <script>
     ''' + script + '''
    </script>
    ''' + add_Image_Map + '''
  </head>

  <body class = "body_ID">
    ''' + add_header + '''
    ''' + body + '''
  </body>
</html>'''

if debug: print(html_string)

f = open("index.html","w")
f.write(html_string)
f.close()
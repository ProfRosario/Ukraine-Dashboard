import yaml
import json
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
# Updated 2/9/2024 
#      Changed YAML file format removed the the variables idxxxx from the YAML file and updated source code to read new YAML file. 
#      Assigned a default value to the style variable. This corrected the issue when no config data were found or missing
#      Added try-except to catch error when reading the YAML file. If a YAML does exsist, added a default demo file.
#      fixed error with addImageMap command
#      Corrected a TypeError: can only concatenate str (not "int") to str at addEvent command. id is a number not a string str(id) TODO rename id to index
#      Corrected default_table_style issue in yaml file. Commended the first default_style TODO remove repetition. 
# Updated 2/10/24 : Corrected and exeption error opening a file with a variable not initialized.

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

# TODO Remove default constant with default YAML file 2/8/24
default_max_columns  = 4
default_table_style = 'border: 5px dotted orange; border-radius: 10px; background-color: transparent; table-layout: fixed; width: 70% ; margin: 0px auto;'
default_th_style = 'border: 8px dotted green;'
default_tr_style = 'border: 5px solid blue; border-radius: 10px; width: auto; height: 60px;'
default_td_style = 'border: 5px dotted red; border-radius: 10px; background-color:transparent; padding:10px; text-align:center; font-size: 18px; '

default_body_style = 'border: 5px solid grey; border-radius: 10px; padding: 25px; background-image: url("./images/background1.jpg"); background-repeat: no-repeat; background-attachment: fixed; background-size: 100%;'
default_div_style = 'border: 2px solid green; border-radius: 10px; background-color: transparent; padding: 5px;'



default_img_style = 'width: 70%; height: 75px; box-shadow: 0px 0px 20px #888; border-radius: 15px;' # not used 2/8/24 TODO
default_img_style_Header = 'width: 65%; height: 180px; display: block; margin-left: auto; margin-right: auto; box-shadow: 0px 0px 20px #888;  border: 4px dotted green; border-radius: 15px;'
default_img_style_addItem = 'width: 70%; height: 75px; border: 4px dashed orange; border-radius: 15px; box-shadow: 5px 0px 20px #888;'

default_p_style =  'margin: 5px 0px 0px; font-size: 14px; font-family: sans-serif ; text-align: center; font-weight: normal ; font-style: italic; color: blue;' # only used in one location TODO
default_p_style_addTitle = 'width: 75%; font-size: 28px; height: auto; margin-left: auto; margin-right: auto; text-align: center; color: black; font-family: sans-serif; font-weight: bold; font-style: normal; border: 3px dotted blue; border-radius: 10px; background-color: yellow;'
default_p_style_ReturnLink = 'text-align: center; vertical-align: middle; color: black; font-size: 16px; font-family: Times New Roman; font-weight: bold; font-style: italic; border: 3px dotted red; border-radius: 5px; background-color: transparent; box-shadow: 5px 0px 20px #888; width: 25%; height: auto; margin: 5px auto 5px auto;'
default_p_style_addItem =  'text-align: center; color: blue; font-size: 12px; font-family: sans-serif; font-weight: normal; font-style: italic; margin: 0px 0px 0px;'
default_p_style_TimeStamp = 'text-align: center; vertical-align: middle; color: black; font-size: 16px; font-family: Times New Roman; font-weight: bold; font-style: italic; border: 3px dotted blue; border-radius: 7px; background-color: transparent; box-shadow: 5px 0px 20px #888; width: 25%; height: auto; margin: 5px auto 5px auto;'
default_p_style_ReturnLik = 'text-align: center; vertical-align: middle; color: black; font-size: 16px; font-family: Times New Roman; font-weight: bold; font-style: italic; border: 3px dotted red; border-radius: 7px; background-color: transparent; box-shadow: 5px 0px 20px #888; width: 25%; height: auto; margin: 5px auto 5px auto;'

default_target = "_blank"

default_yaml_file = '''
---
Commands:
      - configTable:
              html_title: Demo Dashboard
              debug: "true"

      - addHeaderImage:
              title: banking

      - addReturnLink:
              title: Return to Main Dashboard

      - setMaxColumns:
              max_columns: 3

      - addTitle:
              title: First Title Section

      - addItem:
              title: Add Item 1

      - addItem:
              title: Add Item 2

      - addItem:
              title: Add Item 3

      - addItem:
              title: Add Item 4

      - addItem:
              title: Add Item 5

      - addItem:
              title: Add Item 6

      - addTitle:
              title: Second Title Section

      - setMaxColumns:
              max_columns: 4

      - addItem:
              title: Add Item 7

      - addItem:
              title: Add Item 8

      - addItem:
              title: Add Item 9

      - addItem:
              title: Add Item 10    

      - addTimeStamp:
              title: 'This demo page was created on: '

'''

# default_style = '''
#       .body_ID { ''' + default_body_style + '''}
#       .div_ID { ''' + default_div_style + '''}
#       .table_ID { ''' + default_table_style + '''}
#       .tr_ID { ''' + default_tr_style + '''}
#       .th_ID { ''' + default_th_style + '''}
#       .td_ID { ''' + default_td_style + '''}
#       .p_ID { ''' + default_p_style + '''}
#       '''

# style += default_style

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


try:
    f = open('data.yaml', 'r')
    
    data = yaml.safe_load(f.read())
          
except:
  data = yaml.safe_load(default_yaml_file)

  add_css += '''
    <style> 
        a:link {
        color: white;
        background-color: transparent;
        text-decoration: none;
        }

        a:visited {
        color: white;
        background-color: transparent;
        text-decoration: none;
        }

        a:hover {
        color: green;
        background-color: transparent;
        text-decoration: underline;
        font-weight: bold;
        }

        a:active {
        color: yellow;
        background-color: transparent;
        text-decoration: underline;
        }
    </style>'''
      
# except yaml.YAMLError as exception:

#   print('======> Oops, error opening or reading YAML file \n')
#   print('exception error code = ', exception)
#   f.close()



for id in range(len(data['Commands'])):
#------------------- Command configTable --------------------------
    if 'configTable' in data['Commands'][id]:

      COMMAND = 'configTable'
      if debug: print("Command = " + COMMAND)

      close_all_tags()

      try:
        if 'html_title' in data['Commands'][id][COMMAND]: html_title = data['Commands'][id][COMMAND]['html_title']

        if 'table_style' in data['Commands'][id][COMMAND]: default_table_style = data['Commands'][id][COMMAND]['table_style']

        if 'th_style' in data['Commands'][id][COMMAND]: default_th_style = data['Commands'][id][COMMAND]['th_style']

        if 'tr_style' in data['Commands'][id][COMMAND]: default_tr_style = data['Commands'][id][COMMAND]['tr_style']

        if 'td_style' in data['Commands'][id][COMMAND]: default_td_style = data['Commands'][id][COMMAND]['td_style']

        if 'div_style' in data['Commands'][id][COMMAND]: default_div_style = data['Commands'][id][COMMAND]['div_style']

        if 'body_style' in data['Commands'][id][COMMAND]: default_body_style = data['Commands'][id][COMMAND]['body_style']

        if 'p_style' in data['Commands'][id][COMMAND]: default_p_style = data['Commands'][id][COMMAND]['p_style']

        if 'target' in data['Commands'][id][COMMAND]: default_target = data['Commands'][id][COMMAND]['target']

        if 'debug' in data['Commands'][id][COMMAND]: debug = data['Commands'][id][COMMAND]['debug']

        if debug : print("Command = " + COMMAND)

      except:
        html_title = "Config - YAML Error"
        debug = True
      
      style = ''
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
    elif 'addHeaderImage' in data['Commands'][id]:

      COMMAND = 'addHeaderImage'
      if debug: print("Command = " + COMMAND)
      
      close_all_tags()

      title = ''
      image = './images/noimagefound.png'
      link = ''
      img_style = default_img_style_Header
      div_style = default_div_style
      target = default_target
 
      try:
        if 'title' in data['Commands'][id][COMMAND]: title = data['Commands'][id][COMMAND]['title']

        if 'image' in data['Commands'][id][COMMAND]: image = data['Commands'][id][COMMAND].get('image', './images/noimagefound.png')

        if 'link' in data['Commands'][id][COMMAND]: link = data['Commands'][id][COMMAND]['link']
        
        if 'img_style' in data['Commands'][id][COMMAND]: img_style = data['Commands'][id][COMMAND]['img_style']      

        if 'div_style' in data['Commands'][id][COMMAND]: div_style = data['Commands'][id][COMMAND]['div_style']

        if 'target' in data['Commands'][id][COMMAND]: target = data['Commands'][id][COMMAND]['target']

      except:
        title = 'YAML Error'
        image = './images/noimagefound.png'
        link = ''
        img_style = default_img_style_Header
        div_style = default_div_style
        target = default_target


      if len(image) < 5: alt_title = image = './images/noimagefound.png'

      alt_title = image

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
    elif 'addStyle' in data['Commands'][id]:

      COMMAND = 'addStyle'
      if debug: print("Command = " + COMMAND)
      
      try:
        if 'style' in data['Commands'][id][COMMAND]:
          css_style = data['Commands'][id][COMMAND]['style']
          add_css += '''
      <style> 
          ''' + css_style + '''
      </style>'''
        
        if 'file_name' in data['Commands'][id][COMMAND]:
          file_name = data['Commands'][id][COMMAND]['file_name']
          file = open(file_name, "r")
          add_css += '''
      <style> 
          ''' + file.read() + '''
      </style>'''
          file.close()
      
      except:
        print('addStyle YAML Error')

# ---------------- addScript ---- ------------
    elif 'addScriptXML' in data['Commands'][id]:

      COMMAND = 'addScriptXML'
      if debug: print("Command = " + COMMAND)

      try:
        if 'script' in data['Commands'][id][COMMAND]:
          script = data['Commands'][id][COMMAND]['script']
          add_script += ''' 
          ''' + script + '''
          '''

        if 'file_name' in data['Commands'][id][COMMAND]:
          file_name = data['Commands'][id][COMMAND]['file_name']
          file = open(file_name, "r")
          add_script += ''' 
          ''' + file.read() + '''
          '''
          file.close()
      except:
        if debug: print('addScriptXML YAML Error')
      
# ---------------- addLink ----------------
    elif 'addLinkXML' in data['Commands'][id]:

      COMMAND = 'addLinkXML'
      if debug: print("Command = " + COMMAND)

      try:
        if 'link' in data['Commands'][id][COMMAND]:
          link = data['Commands'][id][COMMAND]['link']
          add_link += ''' 
          ''' + link + '''
          '''

        if 'file_name' in data['Commands'][id][COMMAND]:
          file_name = data['Commands'][id][COMMAND]['file_name']
          file = open(file_name, "r")
          add_link += ''' 
          ''' + file.read() + '''
          '''
          file.close()
      except: 
        if debug: print('addLinkXML YAML Error')
               
#---------------------Command addMeta data ------------------------  
    elif 'addMetaXML' in data['Commands'][id]:

      COMMAMD = 'addMetaXML'
      if debug: print("Command = " +  COMMAND)

      try:
        if 'meta' in data['Commands'][id][COMMAND]:
          meta = data['Commands'][id][COMMAND]['meta']
          add_meta += ''' 
          ''' + meta + '''
          '''

        if 'file_name' in data['Commands'][id][COMMAND]:
          file_name = data['Commands'][id][COMMAND]['file_name']
          file = open(file_name, "r")
          add_meta += ''' 
          ''' + file.read() + '''
          '''
          file.close()
      except:
        if debug: print('addMetaXML YAML Error')
  
#---------------------Command addJavaScript -----------------------
    elif 'addJavascript' in data['Commands'][id]:

      COMMAND = 'addJavascript'
      if debug: print("Command = " + COMMAND)    
      
      try:
        if 'script' in data['Commands'][id][COMMAND]:
          javascript = data['Commands'][id][COMMAND]['script']
          add_java += '''
      <script> 
          ''' + javascript+ '''
      </script>'''

        if 'file_name' in data['Commands'][id][COMMAND]:
          file_name = data['Commands'][id][COMMAND]['file_name']
          file = open(file_name, "r")
          add_java += '''
      <script> 
          ''' + file.read() + '''
      </script>'''
          file.close()
      
      except:
       if debug: print('addJavascript YAML Error')
    

#---------------------Command addReturnLink -----------------------
    elif 'addReturnLink' in data['Commands'][id]: 

      COMMAND = 'addReturnLink'
      if debug: print("Command = " + COMMAND)
      
      close_all_tags() 

      title = ''
      link = ''
      p_style = default_p_style_ReturnLink
      div_style = default_div_style
      target = default_target
      
      try:
        if 'title' in data['Commands'][id][COMMAND]: title = data['Commands'][id][COMMAND]['title']
          
        if 'link' in data['Commands'][id][COMMAND]: link =  data['Commands'][id][COMMAND]['link']

        if 'p_style' in data['Commands'][id][COMMAND]: p_style = data['Commands'][id][COMMAND]['p_style']

        if 'div_style' in data['Commands'][id][COMMAND]: div_style = data['Commands'][id][COMMAND]['div_style']

        if 'target' in data['Commands'][id][COMMAND]: target = data['Commands'][id][COMMAND]['target']
      except:
        if debug: print('addReturnLink YAML Error')

        title = 'addReturnLink YAML Error'
        link = ''
        p_style = default_p_style_ReturnLink
        div_style = default_div_style
        target = default_target
      
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
     
# # -------------------Command addTimeStamp -------------------------
#     elif data['Commands'][id]['command'] == 'addTimeStamp':
    elif 'addTimeStamp' in data['Commands'][id]:

      COMMAND = 'addTimeStamp'
      if debug: print("Command = " + COMMAND)  
  
      close_all_tags()

      title = ''
      p_style = default_p_style_TimeStamp
      div_style = default_div_style

      try:
        if 'title' in data['Commands'][id][COMMAND]: title = data['Commands'][id][COMMAND]['title']
        
        if 'p_style' in data['Commands'][id][COMMAND]: p_style = data['Commands'][id][COMMAND]['p_style']

        if 'div_style' in data['Commands'][id][COMMAND]: div_style = data['Commands'][id][COMMAND]['div_style']
      except:
        if debug: print('addTimeStamp YAML error')
        title = 'YAML Error '
        p_style = default_p_style_TimeStamp
        div_style = default_div_style

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
        <p class = "''' + p_ID + ''' ">''' + title + ' ' + dateCreated + '''</p>
    </div>
    '''

#------------------- Command addTitle------------
    elif 'addTitle' in data['Commands'][id]:

      COMMAND = 'addTitle'
      if debug: print("Command = " + COMMAND)  

      close_all_tags()

      title = ''
      p_style = default_p_style_addTitle
      div_style = default_div_style
  
      try:
        if 'title' in data['Commands'][id][COMMAND]: title =  data['Commands'][id][COMMAND]['title']
  
        if 'p_style' in data['Commands'][id][COMMAND]: p_style = data['Commands'][id][COMMAND]['p_style']
  
        if 'div_style' in data['Commands'][id][COMMAND]: div_style = data['Commands'][id][COMMAND]['div_style']
      except:
        if debug: print('addTitle YAML Error')
        title = 'AddTitle YAML Error'
        p_style = default_p_style_addTitle
        div_style = default_div_style

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
      <p class = " ''' + p_ID + ''' ">''' + title + '''</p>  
    </div>
    '''

#------------------- Command Set Max Columns ----------------------
    elif 'setMaxColumns' in data['Commands'][id]:

      COMMAND = 'setMaxColumns'
      if debug: print("Command = " + COMMAND) 

      close_all_tags()
      
      try:
        if 'max_columns' in data['Commands'][id][COMMAND]: max_columns = data['Commands'][id][COMMAND]['max_columns']
      except:
        if debug: print('setMaxColumns YAML Error')
        max_columns = default_max_columns
      
      if debug: print("Command = " + COMMAND + "; max_columns = " + str(max_columns))  

#--------------------Command addItem --------------------------------- 
    elif 'addItem' in data['Commands'][id]:

      COMMAND = 'addItem' 
      if debug: print("Command = " + COMMAND)  

      title = 'YAML Error'
      image = './images/noimagefound.png'
      p_style = default_p_style
      img_style = default_img_style_addItem
      link = ''
      div_style = default_div_style
      target = default_target

      try:
        if 'title' in data['Commands'][id][COMMAND]: title = data['Commands'][id][COMMAND]['title']

        if 'image' in data['Commands'][id][COMMAND]: image = data['Commands'][id][COMMAND]['image']

        if 'p_style' in data['Commands'][id][COMMAND]: p_style = data['Commands'][id][COMMAND]['p_style']
        
        if 'img_style' in data['Commands'][id][COMMAND]: img_style = data['Commands'][id][COMMAND]['img_style']
      
        if 'link' in data['Commands'][id][COMMAND]: link = data['Commands'][id][COMMAND]['link']
    
        if 'div_style' in data['Commands'][id][COMMAND]: div_style = data['Commands'][id][COMMAND]['div_style']

        if 'target' in data['Commands'][id][COMMAND]: target = data['Commands'][id][COMMAND]['target']

      except:
        title = 'YAML Error'
        image = './images/noimagefound.png'
        p_style = default_p_style
        img_style = default_img_style_addItem
        link = ''
        div_style = default_div_style
        target = default_target

      if len(image) < 5: image = './images/noimagefound.png'

      alt_title = image
              
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

      #if debug: print('=======>Count = ', count_Column)

      if count_Column == max_columns:
        reset_tr()
        reset_count()
        body += '''
        </tr>''' 

#------------------Command  addImageMap -------------------------
    elif 'addImageMap' in data['Commands'][id]:

      COMMAND = 'addImageMap'
      if debug: print("Command = " + COMMAND)  

      close_all_tags()

      title = ''
      image = './images/noimagefound.png'
      use_map = ''
      add_Image_Map += ''
      file_name = ''
      img_style = default_img_style_Header
      div_style = default_div_style

      try:
        if 'title' in data['Commands'][id][COMMAND]: title = data['Commands'][id][COMMAND]['title']
        
        if 'image' in data['Commands'][id][COMMAND]: image = data['Commands'][id][COMMAND]['image']

        if 'use_map' in data['Commands'][id][COMMAND]: use_map = data['Commands'][id][COMMAND]['use_map']
        
        if 'map_style_html' in data['Commands'][id][COMMAND]: add_Image_Map += data['Commands'][id][COMMAND]['map_style_html']
        
        if 'img_style' in data['Commands'][id][COMMAND]: img_style = data['Commands'][id][COMMAND]['img_style']

        if "div_style" in data['Commands'][id][COMMAND]: div_style = data['Commands'][id][COMMAND]['div_style']

        if 'file_name' in data['Commands'][id][COMMAND]: 
          file_name = data['Commands'][id][COMMAND]['file_name']
          file = open(file_name, "r")
          add_Image_Map += file.read()
          file.close()
      except:
        if debug: print('AddImageMap YAML Error')
        title = "YAML Error"
        image = './images/noimagefound.png'
        use_map = ''
        add_Image_Map += ''
        file_name = ''
        img_style = default_img_style_Header
        div_style = default_div_style

      if len(image) < 5:  image = './images/noimagefound.png'
  
      alt_title = image

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
    elif 'addToDo' in data['Commands'][id]:

      COMMAND = 'addToDo'
      if debug: print("Command = " + COMMAND)  

      title = "no title"
      date_start = " "    
      date_end = " "
      complete = "no"
      div_style = default_div_style
      p_style = default_p_style

      try:
        if 'title' in data['Commands'][id][COMMAND]: title = data['Commands'][id][COMMAND]['title']

        if 'date_start' in data['Commands'][id][COMMAND]: date_start = data['Commands'][id][COMMAND]['date_start']

        if 'date_end' in data['Commands'][id][COMMAND]: date_end = data['Commands'][id][COMMAND]['date_end']

        if 'complete' in data['Commands'][id][COMMAND]: complete = data['Commands'][id][COMMAND]['complete']

        if 'p_style' in data['Commands'][id][COMMAND]: p_style = data['Commands'][id][COMMAND]['p_style']

        if "div_style" in data['Commands'][id][COMMAND]: div_style = data['Commands'][id][COMMAND]['div_style']
      
      except:
        if debug: print('AddToDo YAML Error')
        title = "YAML Error"
        date_start = " "    
        date_end = " "
        complete = "no"
        div_style = default_div_style
        p_style = default_p_style
      
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

    elif  'addEvent' in data['Commands'][id]:
      
      COMMAND = 'addEvent'
      if debug: print("Command = " + COMMAND) 
      
      # close_all_tags() 
      
      name = " "
      badge = " "
      date_ = " "
      description = " "
      type = " "
      color = " "
      everyYear = ""
      div_style = default_div_style

      #if debug: print('Command = ' + data['Commands'][id][COMMAND]['command'])

      try:
        if 'name' in data['Commands'][id][COMMAND]: name = data['Commands'][id][COMMAND]['name']

        if 'badge' in data['Commands'][id][COMMAND]: badge = data['Commands'][id][COMMAND]['badge']

        if 'date' in data['Commands'][id][COMMAND]:  date_ = data['Commands'][id][COMMAND]['date']
        
        if 'description' in data['Commands'][id][COMMAND]: description = data['Commands'][id][COMMAND]['description']

        if 'type' in data['Commands'][id][COMMAND]: type = data['Commands'][id][COMMAND]['type']

        if 'color' in data['Commands'][id][COMMAND]: color = data['Commands'][id][COMMAND]['color']

        if 'everyYear' in data['Commands'][id][COMMAND]: everyYear = data['Commands'][id][COMMAND]['everyYear']

        if 'div_style' in data['Commands'][id][COMMAND]: div_style = data['Commands'][id][COMMAND]['div_style']

      except:
        if debug: print('AddEvent YAML Error')

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
                    id: "''' + str(id) + '''",
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
# coding=utf-8
import datetime

# ADD PRODUCT AND COUNT HERE TO PRINT
item = {
    'Tomato Rasam - Made with Organic Lentil': 10,
    'Cabbage Peas': 10,
    'Tawa bhaji (No buns) - Delicacy of Mumbai': 10,
    'Punjabi Kadhi Pakoda - Made with Organic Yogurt': 50,
    'Kala Chana Masala - Made with Organic Black Chickpeas': 10,
    'Creamy Paneer Mix Veg Curry - Made with In-house Organic Paneer and organic veggies': 20,
    'Quinoa Lentil Khichdi - A complete meal in itself (All Organic )': 50,
}


def get_item_div(product_name):
    name = product_name.split(" - ")[0]
    return '<div class="label">' + name + '</div>'


def get_page_break():
    return '''<div class="page-break">&nbsp;</div><div style="margin-top:0.5in"></div>'''


def print_item_labels():
    i = 0
    labels = ""
    for product_name, print_count in item.iteritems():
        for x in range(print_count):
            i = i + 1
            labels = labels + get_item_div(product_name)
            if i % 80 == 0:  # page break
                labels = labels + get_page_break()
                i = 0
    return labels


head = '''<head>
  <meta charset="utf-8">
  <link href="labels.css" rel="stylesheet" type="text/css">
  <style>
    body {
      /*paper width*/
      width: 8.5in;
      /*papersheet margin */
      margin-top: 0.5in;
      margin-bottom: 0.5in;
      /* outline: 1px dotted; */
    }

    .label {
      /* Avery 5160 labels -- CSS and HTML by MM at Boulder Information Services */
      width: 1.65in;
      /* plus .6 inches from padding */
      height: 0.40in;
      margin-left: 0.3in;
      padding: 0.05in 0.05in 0.05in 0.05in;
      /* the gutter */
      display: inline-block;
      float: left;
      font-size: 12px;
      vertical-align: middle;
      font-weight: bold;


      text-align: center;
      overflow: hidden;
      border-radius: 5px;
       /* outline: 1px dotted; */

    }
    .page-break {
      page-break-after: left;
      margin-top: 0.5in;
    }
  </style>
</head>'''


def get_html():
    content = '<html lang="en">'
    content = content + head
    content = content + '<body>'
    content = content + print_item_labels()
    content = content + '</body>'
    content = content + '</html>'
    return content


def print_in_html():
    current_time = datetime.datetime.now()
    created_at = current_time.strftime("%H_%M")
    f = open('item_label_' + created_at + '.html', "w")
    f.write(get_html())
    f.close()


print_in_html()

#Exchange-Website-Django

## <a name="pp">Table of Contents</a>
* [Preface](#Preface)
* [Goals](#Goals)
* [Maintaining](#Maintaining)
* [Meaning of Functions](#MeaningofFunctions)
 
## <a name="Preface">Preface</a> [&#8593;](#pp)

This is the documentation for the new website called Chapull Market, which was created on spring term of
2014 [Bilgi University Computer Science Web Project]


This website is designed on purpose to help people recycle their items through a web site that users. Recycling in this project context means exchange of items. Users have to register the website in order to see information on the web site and recycle. There is a table which shows all items are available to recycle on home page. Users see information about any items such as photograph, model, state, status etc. then users should press more button or click the item’s photo which redirects the users to item detail page. Users also create their own items for recycling the other users items. Each item of users are shown on their profile page. Users can give offer to all other users’ items with recycling own items. Each offers of items are shown on profile page and users can accept or reject the offers of for each own items. The following three sections discuss the design goals, maintaining the site, examples of the pages and functions of the codes.

## <a name="Goals">Goals</a> [&#8593;](#pp)

When designing the new website, here are the goals we had in mind:


**A. Provide a user page with info for registered people**
* Include all items that are available for recycling.
* Include search area that name of searching item to be recycled.
* Include login and register button.
* Provide “profile” link that users can see their all own items.
* Provide “add item” link that user to direct create an item.
* Include logout button.


**B. Visual design**
* Provide a uniform look­and­feel for all pages on the site.
* Use colors compatible with the UMD logo (gray, red, white).
* Don't use frames.
* Make the pages usable even on small (800 pixel width) screens.
* Try to make the page layout work for multiple web browsers and multiple platforms.


**C. Maintenance**
* Try to clean up the directory structure for the site.
* Use modular structure for page elements, to facilitate updating of the pages.
* Try to make it easy to edit the pages with text editor.


## <a name="Maintaining">Maintaining</a> [&#8593;](#pp)

Our main tool for building the new site has been Django. 


Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Developed in 2003 by a fast moving online news operation, Django was designed to handle two challenges: the intensive deadlines of a newsroom and the stringent requirements of the experienced Web developers who wrote it. It lets you build high performing, elegant Web applications quickly. Django is an Open Source web framework that enables you to build clean and feature rich web applications with minimal time and effort.


Django promotes the use of human readable urls.


Django offers the flexibility to customize pieces of the web site to suit the needs of the project at hand instead of relying on pre-built applications. Using Django, we can customize that widget to display what we want, how we want.


Because of the way that Django is developed and installed, you have a greater level of security when you compare it to a website that was developed with PHP for example. This is because the source code, excluding the html and css files, for your web site are not directly exposed to the Internet and your viewers online. In most cases the web pages are dynamically generated and then sent to your browser using templates.


The templates that we develop are for creating a look and feel specific to your website. We are not just filling in information in a template that we downloaded off of another site. Therefore you are guaranteed that the site we develop for you will look unique. This is one of the big features of Django.


Using this template structure makes it much easier for us to add additional pages as well as make site wide, visual or code changes. The template structure also ensures that your website will have a consistent look and feel throughout the entire site.


## <a name="MeaningofFunctions">Meaning of Functions</a> [&#8593;](#pp)

* **add_item(request):**
To create an new item.
*It requires login.*
* **listing (request):**
Shows all available item with pagination.
*It requires login.*
* **item_detail(request, event_id):**
Shows details of selected item.
*It requires login.*
* **search(request):**
To search all existing items with name, brand or description.
*It requires login.*
* **aboutus(request):**
Shows developers’ name.
*It requires login.*
* **exit(request):**
To logout.
*It requires login.*

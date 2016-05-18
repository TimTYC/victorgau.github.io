Title: Setting up Pelican for Github Pages
Date: 2015-11-12 16:38
Tags: Python, Pelican
Category: Python
Slug: setting-up-pelican-for-github-pages
Summary: Setting up pelican for github pages

<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- pelican github -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-3914607163427066"
     data-ad-slot="4932383565"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>

## Installing Pelican:

To install pelican, run the following command.

```python
$ pip install pelican
```

If you plan to use markdown to write articles, please also install markdown.

```python
$ pip install markdown
```

## Creating blog with `pelican-quickstart`:

To create your blog, `cd` to the root directory of your blog and run `pelican-quickstart`

```bash
Victors-MacBook:code victor$ cd blog
Victors-MacBook:blog victor$ pwd
/Users/victor/code/blog
Victors-MacBook:blog victor$ pelican-quickstart
Welcome to pelican-quickstart v3.6.3.

This script will help you create a new Pelican-based website.

Please answer the following questions so this script can generate the files
needed by Pelican.


> Where do you want to create your new web site? [.]
> What will be the title of this web site? Victor Gau
> Who will be the author of this web site? Victor Gau
> What will be the default language of this web site? [en]
> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n)
> What is your URL prefix? (see above example; no trailing slash) http://victorgau.github.io
> Do you want to enable article pagination? (Y/n)
> How many articles per page do you want? [10]
> What is your time zone? [Europe/Paris] Asia/Taipei
> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n)
> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n)
> Do you want to upload your website using FTP? (y/N)
> Do you want to upload your website using SSH? (y/N)
> Do you want to upload your website using Dropbox? (y/N)
> Do you want to upload your website using S3? (y/N)
> Do you want to upload your website using Rackspace Cloud Files? (y/N)
> Do you want to upload your website using GitHub Pages? (y/N) Y
> Is this your personal page (username.github.io)? (y/N) Y
Done. Your new project is available at /Users/victor/code/blog
Victors-MacBook:blog victor$
```

Since I'd like to put my blog onto github, the answers to the github related questions are 'Yes'.

The tree structure after running `pelican-quickstart` is as follows:

```bash
Victors-MacBook:blog victor$ tree
.
├── Makefile
├── content
├── develop_server.sh
├── fabfile.py
├── output
├── pelicanconf.py
└── publishconf.py

2 directories, 5 files
Victors-MacBook:blog victor$
```

There are two configuration files in the directory:

`pelicanconf.py` is intended to be used for previewing.

`publishconf.py` is intended to be used for publishing.


`Makefile` and `fabfile.py` are intended for automation.

`content` is the directory for the source code of your articles.

`output` is the directory for compilation output, i.e., the html files of your static blog.


## Pelican Themes:

You can easily change the style of your blog by setting a specific theme in the configuration file.

To do so, you need to download the themes first.

You can do it by running the following command.

```python
$ git clone --recursive https://github.com/getpelican/pelican-themes ./pelican-themes
```

After downloading the theme files, put the following line in `pelicanconf.py` or `publishconf.py` to use the theme.

```python
THEME = "pelican-themes/pelican-bootstrap3"
```


## Plugins:

Pelican supports varied plugins.  You can use the plugin to render math equations, embed iPython notebook into the post, etc.

To use plugins, download them first by running the following command.

```python
git clone https://github.com/getpelican/pelican-plugins.git
```

And then, put the following settings into `pelicanconf.py` or `publishconf.py`.

The following is an example to use `render_math` plugin.


```python
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['render_math']
```

Testing Math Equation: $E=MC^2$

If you are using markdown, syntax highlighting is already supported.

Testing Syntax Highlighting:

```python
a = 1
b = 2
print a+b
```

## Fabric:

To use fabric for blog automation, please reference to [Nafiul's article](http://nafiulis.me/making-a-static-blog-with-pelican.html).


## Disqus:

Most pelican themes natively support disqus to allow people comment on your post.

To use disqus, you need to register an account at [disqus.com](https://disqus.com/).

And then, add your site from `disqus.com/admin` to get your sitename.

Add the sitename into the configuration file, `pelicanconf.py` or `publishconf.py`.

```bash
DISQUS_SITENAME = 'YourSiteName'
```

After setting the `DISQUS_SITENAME` and re-compilation, You should see disqus comment at the end of your post.

Note that you would not see disqus comment when testing in the local environment.


## References:

* [Install and deploy a Pelican blog using Fabric - Part 1: local environment](http://blog.osteel.me/posts/2015/02/24/install-and-deploy-a-pelican-blog-using-fabric-part-1-local-environment.html)
* [Install and deploy a Pelican blog using Fabric - Part 2: installation and configuration](http://blog.osteel.me/posts/2015/02/26/install-and-deploy-a-pelican-blog-using-fabric-part-2-installation-and-configuration.html)
* [Install and deploy a Pelican blog using Fabric - Part 3: Fabric](http://blog.osteel.me/posts/2015/03/02/install-and-deploy-a-pelican-blog-using-fabric-part-3-fabric.html)
* [Install and deploy a Pelican blog using Fabric - Part 4: workflow, extras and conclusion](http://blog.osteel.me/posts/2015/03/04/install-and-deploy-a-pelican-blog-using-fabric-part-4-workflow-extras-and-conclusion.html)
* [Making a Static Blog with Pelican](http://nafiulis.me/making-a-static-blog-with-pelican.html)
* [Configuring Pelican Static Blog](http://pbpython.com/pelican-config.html)

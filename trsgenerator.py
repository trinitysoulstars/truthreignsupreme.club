#!/usr/bin/env python
""" Generate The Corpus Cloud with Page Elements, to be Styled """

import jinja2
import arrow

corpus = {
        "5Cars": "http://5cars.world",
        "Astral Seed": "http://trinitysoulstars.com",
        "Ascension Symptoms": "http://ascension.fyi",
        "Amethyst Grills": "http://amethystgrills.com/",
        "Bubblin": "http://bubblin.life",
        "Clouds": "http://clouds.zone",
        "Crystal God": "http://thecrystalgod.com/",
        "decause": "http://twitter.com/remy_d",
        "Five Cars": "http://5cars.world",
        "Guarav": "http://trinitysoulstars.com",
        "Higher Self": "http://highself.solutions",
        "Juice Brew": "http://juicebrew.life",
        "LightBody": "http://lightbodytherapy.life",
        "Manifest": "http://trinitysoulstars.com",
        "Mt Meru": "http://mtmeru.life",
        "Nino": "http://nino.movie",
        "Realms": "http://trinitysoulstars.com",
        "Starseed": "http://trinitysoulstars.com",
        "Soulstar": "http://trinitysoulstars.com",
        "Theosyn": "http://trinitysoulstars.com",
        "TRS": "http://truthreignsupreme.club",
        "Source": "http://github.com/trinitysoulstars",
        }

terms = []
titles = ["Welcome to the Trinity Node - the most lit sector in the multiverse"]
metadesc = ["Welcome to the Trinity Node - the most lit sector in the multiverse"]
authors = ["Trinity Soulstars - https://github.com/trinitysoulstars"]
videos = ['<iframe width="560" height="315" src="https://www.youtube.com/embed/lRQGn1f5pYQ" frameborder="0" allowfullscreen></iframe>']
boldwords = {
        "Truth Reign Supreme": "http://truthreignsupreme.club",
        }


# analytics = ['''
#     <!-- Piwik -->
#     <script type="text/javascript">
#       var _paq = _paq || [];
#       _paq.push(["setDomains", ["*.http//www.truthreignsupreme.club"]]);
#       _paq.push(["trackPageView"]);
#       _paq.push(["enableLinkTracking"]);
#       (function() {
#         var u="//piwik-decause.rhcloud.com/";
#         _paq.push(["setTrackerUrl", u+"piwik.php"]);
#         _paq.push(["setSiteId", "6"]);
#         var d=document, g=d.createElement("script"), s=d.getElementsByTagName("script")[0];
#         g.type="text/javascript"; g.async=true; g.defer=true; g.src=u+"piwik.js"; s.parentNode.insertBefore(g,s);
#       })();
#     </script>
#     <noscript><p><img src="//piwik-decause.rhcloud.com/piwik.php?idsite=6" style="border:0;" alt="" /></p></noscript>
#     <!-- End Piwik Code -->
#     ''',
#     ]


for term, link in corpus.iteritems():
    print term, link
    terms.append(term)

print "terms =  %s " % terms
print "titles = %s " % titles
print "metadesc = %s " % metadesc
print "authors = %s " % authors
print "videos = %s " % videos
#print "analytics = %s " % analytics

for term, link in boldwords.iteritems():
    print term, link


template = jinja2.Template("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

<title>
    {%- for title in titles: -%}
        {{title}}
    {%- endfor -%}
    </title>

<meta name="description" content="
    {%- for desc in metadesc: -%}
        {{desc}}
    {%- endfor -%}"/>

<meta name="keywords" content="
    {%- for term in terms: -%}
        {{term}},
    {%- endfor %}"/>

<meta name="author" content="
    {%- for author in authors: -%}
        {{author}}
    {%- endfor -%}"/>
<link rel="stylesheet" type="text/css" href="style.css" media="screen"/>

    <!-- Bootstrap Core CSS -->
    <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom Fonts -->
    <link href="vendor/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">

    <!-- Theme CSS -->
    <link href="css/grayscale.min.css" rel="stylesheet">

    <!-- Font for Stars Background -->
    <link href='http://fonts.googleapis.com/css?family=Lato:300,400,700' rel='stylesheet' type='text/css'>

    <!-- Custom CSS -->
    <link href="css/custom.css" rel="stylesheet" type="text/css">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

    <!-- Piwik -->
    <script type="text/javascript">
      var _paq = _paq || [];
      _paq.push(["setDomains", ["*.http//www.truthreignsupreme.club"]]);
      _paq.push(["trackPageView"]);
      _paq.push(["enableLinkTracking"]);
      (function() {
        var u="//piwik-decause.rhcloud.com/";
        _paq.push(["setTrackerUrl", u+"piwik.php"]);
        _paq.push(["setSiteId", "6"]);
        var d=document, g=d.createElement("script"), s=d.getElementsByTagName("script")[0];
        g.type="text/javascript"; g.async=true; g.defer=true; g.src=u+"piwik.js"; s.parentNode.insertBefore(g,s);
      })();
    </script>
    <noscript><p><img src="//piwik-decause.rhcloud.com/piwik.php?idsite=6" style="border:0;" alt="" /></p></noscript>
    <!-- End Piwik Code -->

</head>

<div id='stars'></div>
<div id='stars2'></div>
<div id='stars3'></div>
<body id="page-top" data-spy="scroll" data-target=".navbar-fixed-top">

    <!-- Navigation -->
    <nav class="navbar navbar-custom navbar-fixed-top" role="navigation">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-main-collapse">
                    Menu <i class="fa fa-bars"></i>
                </button>
                <a class="navbar-brand page-scroll" href="#page-top">
                    <i class="fa fa-codepen"></i> <span class="light">Trinity</span> NODE
                </a>
            </div>

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse navbar-right navbar-main-collapse">
                <ul class="nav navbar-nav">
                    <!-- Hidden li included to remove active class from about link when scrolled up past about section -->
                    <li class="hidden">
                        <a href="#page-top"></a>
                    </li>
                    <li>
                        <a target="_blank" class="page-scroll" href="https://soundcloud.com/trinitysoulstars"><i style="margin-right: 3px;" class="fa fa-soundcloud"></i> <span style="font-size:13px;">SoundCloud</span></a>
                    </li>
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container -->
    </nav>

    <!-- Body -->

    <header class="intro" style="margin-top: 5%;">
        <div class="intro-body">
            <div class="container">
                <div class="row">
                    <div class="col-md-8 col-md-offset-2">
                        <a class="logo" href ="http://trinitysoulstars.com/" target="_blank"><img style="width: 230px;" src="img/logo.png"/></a>

    {% for video in videos: %}
        {{video}},
    {% endfor %}

                        <hr style="margin-top: 8px;margin-bottom: 13px;border: 0;border-top: 1px solid #eee;width: 500px;"/>
                        <p style="margin: 30px 0 40px;"><a style="margin-right:8px:" href="https://www.facebook.com/trinitysoulstars" class="btn btn-circle page-scroll" target="_blank">
                            <i class="fa fa-facebook"></i>
                        </a>
                        <a style="margin-left:4px;margin-right:4px;" href="https://twitter.com/trinitysoulstar" class="btn btn-circle page-scroll" target="_blank">
                            <i class="fa fa-twitter"></i>
                        </a>
                        <a href="https://www.instagram.com/trinitysoulstars/" class="btn btn-circle page-scroll" target="_blank">
                            <i class="fa fa-instagram"></i>
                        </a>
                        </p>
<!-- Tag Cloud -->

<p class='pcloud'>
    {% for term, link in boldwords.iteritems(): -%}
        <a class='boldwords btn-lg' target="_blank" href="{{link}}">{{term}}</a>
    {% endfor -%}
    {% for term, link in corpus.iteritems(): -%}
        <a target="_blank" class="btn-lg" href="{{link}}">{{term}}</a>
    {% endfor %}
</p>


                    </div>
                </div>
            </div>
        </div>
    </header>


    <!-- jQuery -->
    <script src="vendor/jquery/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="vendor/bootstrap/js/bootstrap.min.js"></script>

    <!-- Plugin JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js"></script>

    <!-- Google Maps API Key - Use your own API key to enable the map feature. More information on the Google Maps API can be found at https://developers.google.com/maps/ -->
    <script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCRngKslUGJTlibkQ3FkfTxj3Xss1UlZDA&sensor=false"></script>

    <!-- Theme JavaScript -->
    <script src="js/grayscale.min.js"></script>

</body>
</html>
""")

# When you add new elements to the template, you must define it outside the template, and then pass in the value below
output = template.render(corpus=corpus, terms=terms, titles=titles, metadesc=metadesc, authors=authors, videos=videos, boldwords=boldwords)

with open('{}.html'.format(arrow.now().format()[0:10]), "wb") as f:
        f.write(output)

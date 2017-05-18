.. _`LinuxCMD`:

chapter 4 :AngularJS
============================


4.1 Basic
------------------------



4.1.1 mastering angularjs web application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

01 - hello world

cd 01\ -\ hello\ world/







4.2 Extension
------------------------

npm install
npm install express






4.2.1 AngularJS +Express+NodeJS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ref : http://briantford.com/blog/angular-express

https://github.com/btford/angular-express-seed

https://github.com/angular/angular-seed


body-parser warning

::

    //app.use(bodyParser());
    //app.use(bodyParser.urlencoded());
    app.use(bodyParser.urlencoded({ extended: true }));
    app.use(bodyParser.json());

.

run: npm install express-error-handler
change line 9 to: errorHandler = require('express-error-handler'),
change line 36 to: app.use(errorHandler());

::

    npm install express-error-handler

app.js
::

    //  errorHandler = require('error-handler'),
    errorHandler = require('express-error-handler'),

    //app.use(bodyParser());
    //app.use(bodyParser.urlencoded());
    app.use(bodyParser.urlencoded({ extended: true }));
    app.use(bodyParser.json());


    //app.use(methodOverride());
    app.use(methodOverride());

    //  app.use(express.errorHandler());
    app.use(errorHandler());

.

4.2.2 generator-angular-fullstack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


https://github.com/DaftMonk/generator-angular-fullstack

*cache clean

npm cache clean
bower cache clean



root:

::

    npm install -g generator-angular-fullstack



sean:
::

    mkdir my-new-project && cd $_
    yo angular-fullstack [app-name]

.
Run grunt for building, grunt serve for preview, and grunt serve:dist for a preview of the built app.








4.2.3 npm proxy setting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

npm proxy setting
::

    npm config set proxy http://xx.xx.xx.xx:8080
    npm config set https-proxy http://xx.xx.xx.xx:8080
    npm config set strict-ssl false

.

4.2.4 yoeman
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

https://github.com/yeoman/generator-angular


in root

npm install -g grunt-cli bower yo generator-karma generator-angular  generator-webapp

or
sudo  npm install -g grunt-cli bower yo generator-karma generator-angular generator-webapp

in sean

mkdir my-new-project && cd $_

yo angular [app-name]

npm install

grunt

grunt build

grunt server

modified Gruntfile.js  localhost-->10.3.0.115


4.2.5 malhar-dashboard-webapp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
https://github.com/DataTorrent/malhar-dashboard-webapp



https://github.com/the-lay/zabbix-angularjs


sean
rm -rf /home/sean/.npm/*


sudo npm install  -g grunt-cli

npm install

npm install phantomjs

bower install

grunt




grunt serve

4.2.6 gerator-cg-angular
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
enterprise generator-angularjs
https://github.com/cgross/generator-cg-angular


4.2.7 angularjs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
angularjs

1.install grunt

::

    sudo npm install -g grunt-cli

2. install yoeman
::

        sudo  npm install -g yo


3. install bower
::

    sudo  npm install -g bower

4. install angular generator
::

    sudo npm install -g generator-angular

5. su sean
::

    $ sudo chonw -R user  ~/.npm
    $ su sean
    $ mkdir angularStudy
    $ cd angularStudy
    $ yo angular

    $ grunt server

.
https://github.com/nickholub/angular-dashboard-app

*Running Application


    Node.js way

    Install express

      $ npm install express

    Run Node.js server

      $ node app.js

    Application will be available at http://localhost:3000.

    Simple web server way

    Start any web server in "dist" directory, e.g. with Python

      $ python -m SimpleHTTPServer 8080

    Application will be available at http://localhost:8080
*Running Application (development mode)
Install dependencies:

    $ npm install

stream.js:94
      throw er; // Unhandled stream error in pipe.
            ^
Error: invalid tar file

*install autoconf 2.6.5 by source

./configure --prefix=/usr

make

make check

make install

*install automake 1.14 by source

./configure --prefix=/usr --docdir=/usr/share/doc/automake-1.14.1
make
sed -i "s:./configure:LEXLIB=/usr/lib/libfl.a &:" t/lex-{clean,depend}-cxx.sh
make -j4 check
make install



npm install gulp-imagemin@1.0.1
npm install imagemin@1.0.5
npm install imagemin-gifsicle@1.0.0
npm install gifsicle@1.0.2


Install Bower dependencies:

    $ bower install

Run Grunt server task:

    $ grunt server

Application will be available at http://localhost:9000
*Building Application

pplication is built with Grunt.

    $ npm install -g grunt-cli
    $ grunt


4.2.8 AngularJS +Express+NodeJS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ref : http://briantford.com/blog/angular-express

https://github.com/btford/angular-express-seed

https://github.com/angular/angular-seed


body-parser warning

::

    //app.use(bodyParser());
    //app.use(bodyParser.urlencoded());
    app.use(bodyParser.urlencoded({ extended: true }));
    app.use(bodyParser.json());

.

run: npm install express-error-handler
change line 9 to: errorHandler = require('express-error-handler'),
change line 36 to: app.use(errorHandler());

::

    npm install express-error-handler

app.js
::

    //  errorHandler = require('error-handler'),
    errorHandler = require('express-error-handler'),

    //app.use(bodyParser());
    //app.use(bodyParser.urlencoded());
    app.use(bodyParser.urlencoded({ extended: true }));
    app.use(bodyParser.json());


    //app.use(methodOverride());
    app.use(methodOverride());

    //  app.use(express.errorHandler());
    app.use(errorHandler());

.

4.2.9 generator-angular-fullstack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


https://github.com/DaftMonk/generator-angular-fullstack

*cache clean

npm cache clean
bower cache clean



root:

::

    npm install -g generator-angular-fullstack



sean:
::

    mkdir my-new-project && cd $_
    yo angular-fullstack [app-name]

.
Run grunt for building, grunt serve for preview, and grunt serve:dist for a preview of the built app.





4.2.10 mastering angularjs web application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Modifying the style of HTML Input(type=range) element

We can not modify html Input element with the type of *range* just with CSS only. This type of input element will display a slider. The slider form and color will depend on the rendering engine of our browser. As there was two popular rendering engine known right now, it means we should create two kind of style if we want our slider will display consistenly among the existing browser. As we know the two most popular rendering engine were **webkit** (use by Chrome and its derivative) and **mozilla** (use by Firefox).

There is many way to do that. Here I just want to experiment using a relatively new Python web framework i.e *FastHTML*. With this framework actually we don't need JavaScript and CSS Framework explicitly. FastHTML already incorporated (hide) JavaScript (good news for you who don't want to learn JavaScript for front end development) and Pico CSS Framework in it. It means you can use just Python only to create front-end web application.

However, in this experiment I want to show you how we can still incorporate our own choosen JavaScript and CSS framework. Especially in modifying the input element with the type of range it seems we still need JavaScript to do that.

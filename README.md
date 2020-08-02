# Reimagined Disco

So I'm thinking...

* The API in [`click.secho`](https://click.palletsprojects.com/en/7.x/utils/#ansi-colors) is [neat](https://github.com/GoogleCloudPlatform/django-demo-app-unicodex/blob/master/.util/cliformatting.py). 
* ASCII art is [neat](https://github.com/glasnt/glasnt)
* You can respect HTML headers to treat [curl requests differently](https://github.com/pretalx/pretalx/blob/master/src/pretalx/agenda/views/schedule.py#L176)
* You can define [RGB background and foreground colours](https://mudhalla.net/tintin/info/ansicolor/)

So in theory you can make `ih` display cross-stitch charts in coloured terminal output if you curl a hosted version. 

## Notes

Terminal pixels probably aren't square. Hack: in the 'render' mode, the image is converted to a more visually pleasing aspect ratio. If it's not spaces are used to attempt the same without distorting the exact pixels.

## Progress


```
curl /

 > outputs a test of the colourisation system

curl /img/(filename)

 > outputs the local filename to terminal colorised output. 

Options: 

 * render: if true, renders a full image. If false, renders a stitchable chart.

e.g. curl localhost:8080/img/test_image.png

```

Todo: 

 * Work out if I want to use ih-style API, or asciify. 
 * Incorporate this scratch repo into ih

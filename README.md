# Reimagined Disco

So I'm thinking...

* The API in [`click.secho`](https://click.palletsprojects.com/en/7.x/utils/#ansi-colors) is [neat](https://github.com/GoogleCloudPlatform/django-demo-app-unicodex/blob/master/.util/cliformatting.py). 
* ASCII art is [neat](https://github.com/glasnt/glasnt)
* You can respect HTML headers to treat [curl requests differently](https://github.com/pretalx/pretalx/blob/master/src/pretalx/agenda/views/schedule.py#L176)
* You can define [RGB background and foreground colours](https://mudhalla.net/tintin/info/ansicolor/)

So in theory you can make `ih` display cross-stitch charts in coloured terminal output if you curl a hosted version. 

## Progress

Working on an API for formatting output. 

Todo: 

 * Work out if I want to use ih-style API, or asciify. 
 * Incorporate this scratch repo into ih

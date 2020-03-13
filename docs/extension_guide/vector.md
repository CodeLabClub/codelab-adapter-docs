# Vector
<!--Vector CodeLab-->
>  Anki is a company whose products always seem to delight. 

We love [Cozmo](https://www.anki.com/en-us/cozmo), we love [Vector](https://www.anki.com/en-us/vector).

[Codelab Adapter](https://adapterv2.codelab.club) is a software that connect Scratch3.0 to the open-source hardware, IoT and AI.

We make a [Codelab Adapter](https://adapterv2.codelab.club) extension to connect Vector to Scratch3.0. It just like Cozmo codelab. 

![](/img/scratch3-vector_2b21057e.png)

Now the Vector extension is built into the [Codelab Adapter](https://adapterv2.codelab.club)!


# Video tutorial
### for Windows
<iframe width="640" height="360" src="https://www.youtube.com/embed/PmF10SKTnvk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### for MacOS/Linux

<iframe width="640" height="360" src="https://www.youtube.com/embed/4CVV8LMc9Oc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# Tutorial

### install codelab_adapter_client
Python >= `3.5`

Linux/MacOS user:  `python3 -m pip install codelab_adapter_client --user`

windows user: `python -m pip install codelab_adapter_client --user`

### Install the SDK on your system
Follow Vector official tutorial:  [Initial Setup](https://developer.anki.com/vector/docs/initial.html)

If the following code (`hello_world.py`) runs smoothly, go to the next step.

```python
'''
MacOS:
    /usr/local/bin/python3 hello_world.py
linux:
    /usr/bin/python3 hello_world.py
Windows:
    python hello_world.py
'''
import anki_vector
from codelab_adapter_client import AdapterNode

def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        print("Say 'Hello World'...")
        robot.behavior.say_text("Hello World")


if __name__ == "__main__":
    main()
```




###  Download  Codelab Adapter
<a href="https://adapterv2.codelab.clubuser_guide/install/">Download  Codelab Adapter</a>

run it

<img width=300 src="/img/scratch-adapter_5f5e6f20.png"/>

<!--
### find your local python3 path(Windows users can skip this step)
edit `~/codelab_adapter/extensions/extension_vector.py`, replace python3_path with your local python3 path: `which python3`.

![](/video/scratch-python3-path_37d6feee.png)

restart Codelab Adapter.
-->

### Open Scratch3.0
open [CodeLab Scratch3](https://scratch3v2.codelab.club/)

### Open extension_vector
![](/img/scratch3-vector_3dd2cf42.png)

Ok!

Enjoy it :)


!!! Tip
    Tool for watching the camera feed and test animations of Anki's robot Vector: [Vector-Explorer-Tool](https://github.com/GrinningHermit/Vector-Explorer-Tool)

---

Here are some demo cases（just like Cozmo CodeLab）:

##  Vector and Leap Motion
<video width=300px src="/video/vector_leapmotion.mp4" controls="controls"></video>


## Switch Labo and Vector
<video width=300px src="/video/vector_labo.mp4" controls="controls"></video>

## Candy Language for Vector
<video width=600px src="/video/candy_vector.mp4" controls="controls"></video>




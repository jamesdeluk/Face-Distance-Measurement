# James's README

Note this currently only works on Windows (because of the beep)

1. Download and extract the .zip: https://github.com/jamesdeluk/Face-Distance-Measurement/archive/refs/heads/main.zip
2. Install Python 3.11 (not 3.12 or later): https://www.python.org/downloads/
3. Optional: Create and activate a virtual environment: `python -m venv Face-Distance-Measurement-env` then `Face-Distance-Measurement-env\Scripts\activate`
4. Install requirements: `pip install -r Face-Distance-Measurement-main\requirements.txt`
5. Edit `calculate_f.py` with a text editor (e.g. Notepad) and change:
   1. `d = 50` to the distance you want to be from the screen (in cm)
   2. `W = 6.3` to your pupillary distance (in cm)
6. Run `python calculate_f.py` and watch the console to see the number for `f` (also, if you want, look at your beautiful face in the pop-up)
7. Edit `measure_distance.py` with a text editor (e.g. Notepad) and change:
   1. `f = 700` to the number from `calculate_f.py`
   2. `W = 6.3` to your pupillary distance (in cm)
   3. `limit = 50` to the distance you want to be alerted to if you get too close (in cm)
8. Run `python measure_distance.py`

You can also use `measure_distance_with_face.py` instead (need to make the same Notepad changes) but this will use more power.

# Original README: Face-Distance-Measurement
In this project, we are going to find the distance between a face and a normal webcam. We will use some basic mathematics along with some AI techniques to achieve decent accuracy. To solidify the concept we will use it in an example project, where the size of the text increases if the person is far away from the screen.
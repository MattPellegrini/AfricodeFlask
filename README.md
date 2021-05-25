# First time setup
Create the python virtual environment by running
* `python3 -m venv .` in the top level directory of this project.
* Activate the virtual environment `source bin/activate`
* Install the required python libraries `pip install -r requirements.txt`
* Continue from step 2 in the Running instructions.

# Development setup
Run the following steps each time you start a development session.
* Sync the latest changes.
  * Run `git pull --rebase` or click on the 'Source Control' icon at the far left in Visual Studio, then click on the `...` > `Pull / Push` > `Pull (Rebase)`

# Running
1. In visual studio, click `Terminal` > `New Terminal`.
2. In the termainal that opened, activate the python virtual environment. 
    1. `source bin/active` on linux or run `\path\to\env\Scripts\activate` on windows.
3. Set the environment variables that Flask needs.
    1. `export FLASK_ENV=development` on linux or  `set FLASK_END=development` on windows.
    2. `export FLASK_APP=app` on linux or `set FLASK_APP=app` on windows.
4. To launch the server, run `flask run`
    1. To run so that the server is visible beyond localhost, instead run `flask run --host 0.0.0.0`

# Development setup
Run the following steps each time you start a development session.
* Sync the latest changes.
  * Run `git pull --rebase` or click on the 'Source Control' icon at the far left in Visual Studio, then click on the `...` > `Pull / Push` > `Pull (Rebase)`

# Running
* In visual studio, click `Terminal` > `New Terminal`.
* In the termainal that opened, activate the python virtual environment. 
  * `source bin/active` on linux or run `\path\to\env\Scripts\activate` on windows.
* Set the environment variables that Flask needs.
  * `export FLASK_ENV=development` on linux or  `set FLASK_END=development` on windows.
  * `export FLASK_APP=app` on linux or `set FLASK_APP=app` on windows.
* To launch the server, run `flask run`

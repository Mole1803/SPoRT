# SPoRT (SeaPortRouteTool)


## Frontend setup

**Wichtig NodeJs muss installiert sein.**

Als erstes müssen die angular-cli installiert werden damit Commands ausgeführt werden können:

`npm install -g @angular/cli`

Im nächsten schritt die dependencies installieren 

```
cd SPoRT
cd SeaPortOptimizerFrontend
npm install
```





## Backend setupen und starten
In den Root folder navigieren und dann folgenden Befehl ausführen:

```
# Virtuelles vene erstelllen. py kann auch python oder python3 sein, je nachdem wie python auf dem System konfiguriert ist.

py -m venv venv

# In cmd.exe
venv\Scripts\activate.bat
# In PowerShell
venv\Scripts\Activate.ps1

pip install -r requirements.txt```
```

und anschließend kann der Befehl mit



## Anwendung starten

Zunächst sollte versucht werden die Anwendung mit main.py zu starten.
Sollte dies nicht funktionieren dann folgende Schritte befolgen.



### Frontend starten

```
ng serve --watch
```
ng serve startet die App im Debug Modus


### Backend starten
```
ReplaceWithPathToProject/venv/Scripts/python -m flask run
```

bzw.

```
ReplaceWithPathToProject/venv/Scripts/python -m flask run
```

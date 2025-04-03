# Mein Projekt
[Projektfile](https://github.com/Fynn8962/Python-Alarm-Clock/blob/main/alarmClock/alarm_python.py)                            
Die Python alarm-clock ist eine in Python programmierte Uhr mithilfe der tkinter library. Das Design ist simple gehalten, der Fokus liegt nicht wirklich auf schönem Aussehen. Die hat neben dem Anzeigen der Zeit noch drei weitere Funktionen, einen Wecker, einen Timer und eine Stoppuhr.              
  
<img src="https://github.com/Fynn8962/Python-Alarm-Clock/blob/main/images/python_clock.png" alt="Uhr GUI" width="500" >


**Wecker:** Der Wecker kann auf eine beliebige Zeit gestellt werden und wird dann oben links angezeigt. Wird die Uhrzeit erreicht, ertönt ein Ton und im Fenster wird ein Text angezeigt.             

<img src="https://github.com/Fynn8962/Python-Alarm-Clock/blob/main/images/python_alarm.png" alt="Wecker GUI" width="500" >


**Timer:** Der Timer lässt sich auf die Sekunde genau stellen. Auch dieser läuft im Hintergrund weiter und wird im dazugehörigen Feld angezeigt. Stoppt man den Timer bleibt er in diesem Zustand bis er entweder wieder gestartet oder zurückgesetzt wird.   

<img src="https://github.com/Fynn8962/Python-Alarm-Clock/blob/main/images/python_timer.png" alt="Timer GUI" width="500" >


**Stoppuhr:** Die Stoppuhr zählt die Zeit auf Millisekunden genau nach oben. Im Gegensatz zum Wecker und zum Timer läuft diese zwar im Hintergrund weiter, wird jedoch nicht passiv angezeigt. (Passive Anzeige wird noch folgen, Stand 03.04.2025)                

<img src="https://github.com/Fynn8962/Python-Alarm-Clock/blob/main/images/python_stopwatch.png" alt="Stoppuhr GUI" width="500" >


Die Applikation lässt sich je nach Wünschen des Users benutzen. Man kann alle Funktionen gleichzeitig benutzen oder einfach nur die Zeit sich auf die Sekunde genau anzeigen lassen.

-------------------

# Python Alarm Clock
Fynn Huber              
26.02.2025

&nbsp;

&nbsp;

## Idee
Mithilfe von Python in der IDE Visual Studio Code einen Wecker Programmieren. Der Wecker soll auch eine Benutzeroberfläche haben, wo Informationen angezeigt werden. Funktionen die der Wecker haben soll sind: 
- Uhrzeit anzeigen
- Wecker funktioen (einstellen, auslösen)
- Stoppuhr
- Timer

## Ziel
Ich möchte dieses Projekt meine Python-Kenntnisse erweitern, da ich noch mit viel in der Sprache gearbeitet habe. Ausserdem will ich mehr praktische Erfahrung durch eigene Projekte sammeln.

 &nbsp;

### 26.02.2025
  - [x] Was brauche ich damit ich ein Interface (den "Bildschirm") des Weckers darstellen kann
  - [x] Wie soll dieses Grob aussehen

**Fortschritt**            
Um in Python in GUI zu erstellen habe ich mich für das Tkinter Framework entschieden. Es ist einfach zu benutzen und gut um GUI für applikation zu erstellen. Ich werde mich damit befassen wie das Framework funktioniert wenn ich mit dem Projekt (Coden) anfange.

Um eine Grobe Vorstellung zu haben, habe ich in DrawIO eine kurze Skizze gemacht wie das GUI aussehen könnte.                

<img src="https://github.com/Fynn8962/Python-Alarm-Clock/blob/main/images/AlarmClockPrototype.png" alt="Alarm Clock Prototype" width="500" >

 &nbsp;

### 03.03.2025
  - [x] Testprojekt erstellen, erste Schritte für das Framework.
  - [x] Grundlagen von tkinter verstehen und diese um Testprojekt umsetzen. 

**Fortschritt**  
Ich habe durch den Anfang dieses Youtube Tutorials (https://www.youtube.com/watch?v=mop6g-c5HEY) die Grundlagen von tkinter gelernt und diese in einem Testprojekt notiert. Ich habe das tkinter Framework importiert und zusätzlich das ttkboostrap im mehr Designmöglichkeiten zu haben. Anschliessend habe ich ein erstes Testprojekt mithilfe des Tutorials erarbeitet, welches Kilometer in Meilen umrechnet. Das Testprojekt hat mir geholfen den grundlegenden Syntax von tkinter zu verstehen und wie das Framework aufgebaut ist.                  
Das Testprojekt habe ich hochgeladen.

 &nbsp;

### 05.03.2025
  - [x] Weiter tkinter anhand des Tutorials lernen um ein gutes Grundwissen zu haben

**Fortschritt**  
Da ich bemerkt habe, dass es einfach ist, wenn ich zuerst noch etwas mehr über tkinter lerne, habe ich mich dazu entschieden noch gewisse Themen anhand des Tutorials zu erarbeiten. Dies habe ich in einem neuen Projektordner gemacht, da diese Übungscodes nicht um bedingt schön geschrieben sind und mit vielen Kommentaren versehen.
           

 &nbsp;

### 13.03.2025
  - [x] Anfangen mit dem Alarm Clock Projekt und erste Uhrzeit anzeigen

**Fortschritt**  
Ich habe zuerst damit begonnen ein Grid Layout zu erstellen, in welchem ich meine Alarm Clock darstellen möchte. Anschliessend habe ich den ersten Frame hinzugefügt, in welchem die Uhrzeit angezeigt werden soll. In diesem Frame habe ich dann ein Label platziert, welches die Uhrzeit anzeigt. Die Anzeige und Aktualisierung der Uhrzeit habe ich auf einer Website gefunden, den Code habe ich so angepasst, dass er für meinen Code funktioniert und schon konnte ich die Zeit anzeigen lassen. 
           

 &nbsp;

### 21.03.2025
- [x] Timer Funktion implementieren das bei auslösen ein Effekt oder Ton kommt. 
- [x] Nach dem gleichen Prinzip wie der Timer eine Stopwatch implementieren.

**Fortschritt**  
Zunächst habe ich die Timer-Funktion implementiert, dabei aber anfangs eine ungeeignete Methode gewählt. Ich wollte die Eingabe in nur einem Feld ermöglichen, was die Trennung von Stunden, Minuten und Sekunden erschwert hätte. Deshalb entschied ich mich für drei separate Eingabefelder. Danach gestaltete ich die Benutzeroberfläche für die Stoppuhr und passte das Layout an. Die Implementierung der Stoppuhr-Funktion erwies sich als schwieriger als erwartet, und nach viel probieren verlor ich den Überblick über die Funktionen. Daher entschied ich mich, alles zu entfernen und die Funktion beim nächsten Mal neu zu implementieren.
           

 &nbsp;

### 24.03.2025
- [x] Stopwatch Funktion implementieren (Start, Stop, Reset)

  

**Fortschritt**  
Ich habe mithilfe eines Tutorials und KI die Stoppuhr Funktion implementiert. Ich hatte Probleme mit der Millisekunden Anzeige da diese sehr genau sein muss, damit es Funktioniert. Anfangs war die Zeit zu langsam, da die Millisekunden zu langsam hochgingen. Dann habe ich eben mithilfe von KI erfahren, dass es mit der Methode die ich zuerst angewendet habe durch GUI Updates und CPU-Belastung zu Verzögerung kommen kann. Um dies zu beheben habe ich dann anstelle eines Zählers der sich immer um 1 erhöht die echte vergangene Zeit gemessen, mit der time.time() Methode.  
           

 &nbsp;

### 28.03.2025
- [x] Timer Funktion abändern damit man stoppen und zurücksetzen kann
- [x] Wecker GUI implementieren
- [x] Wecker Funktion hinzufügen



**Fortschritt**  
Zuerst habe ich eine Start, Stopp und Restart Funktion beim Timer hinzugefügt. Ausserdem habe ich beim Clickevent auf das Eingabefeld hinzugefügt, dass es den Text (die vorhandenen Nullen) automatisch markiert. Somit muss man diese nicht herauslöschen, sondern kann einfach seine beliebigen Zahlen eingeben. Anschliessen habe ich eine ähnlich wie Timer und Stoppuhr eine Wecker Benutzeroberfläche hinzugefügt und dazu auch dessen Funktion. Anders als beim Timer oder bei der Stoppuhr läuft der Wecker auch im Hintergrund weiter (was im Button angezeigt wird). Es wäre nun von Vorteil dies auch für den Timer zu übernehmen, jedoch fehlt mir dazu die Zeit, weshalb ich dies ausserhalb der Lernperiode machen werde und es später in der Projektbeschreibung hinzufüge.
           

 &nbsp;

### 01.04.2025
- [x] Eingabeüberprüfung damit keine ungültigen Werte eingegeben werden können
- [x] Timer uach im Hintergrund laufen lassen + Anzeige des Timers im Button
- [x] Code überaurbeiten, Layout, Zeilenabstände etc. (refactoring)

**Fortschritt**  
Ich habe für die Timerfunktion und die Weckerfunktion eine Eingabeüberprüfung implementiert, damit, wenn eine zu grosse Zahl oder ein Buchstabe eingegeben wird, der Wert zurückgesetzt wird. Ausserdem habe ich den Code so geändert, dass der Timer auch weiterläuft, wenn man diesen schliesst. Zusätzlich wird, wenn der Timer im Hintergrund läuft, die verbleibende Zeit im Button des Timers angezeigt. 
Danach habe ich mithilfe von "flake8" den Code PEP8 konform gemacht. Ich habe die meisten Fehler behoben, inklusiven den zu langen Zeilen. Ich finde, das Kürzen der Zeichen hat an manchen Stellen den Code etwas unübersichtlicher gemacht, weshalb ich mir nicht sicher bin, ob es nicht besser wäre dies zurückzurudern. Im hochgeladenen Code sind die Zeilen nach PEP8 gekürzt.

 &nbsp;
  
### 04.04.2025
- [ ] Variabeln überarbeiten damit eine konsistente Namensgebung vorhanden ist


**Fortschritt**  

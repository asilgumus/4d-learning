(function () {
  "use strict";

  const projects = [
    {
      id: "neurobridge",
      index: "01",
      title: "NeuroBridge",
      kicker: "Neuroscience · Accessibility",
      status: "available",
      audience: "Students and STEM clubs",
      duration: "Flexible programme",
      level: "Open to beginners",
      tags: ["Neuroscience", "Accessibility", "Web platform"],
      summary: "Make brain science interactive, open and approachable through accessible demonstrations and digital learning.",
      intro: "NeuroBridge connects neuroscience and accessibility. It turns complex brain science into interactive, web-based STEAM experiences that students can explore regardless of their background or prior knowledge.",
      sourceLinks: [
        { label: "Explore the live platform", url: "https://neurobridge-q1b6atazm-asil-dogan-gumuss-projects.vercel.app/" },
        { label: "View the open-source code", url: "https://github.com/asilgumus/neurobridge" }
      ],
      sections: [
        { title: "Purpose", body: ["Introduce learners to neuroscience and brain-computer interaction through experiences they can see and try.", "Use accessibility as a design requirement from the beginning, not as an addition at the end."], list: ["Turn abstract neuroscience concepts into visible interactions", "Create a welcoming entry point for students with different experience levels", "Encourage teams to build on and share the open-source work"] },
        { title: "Prepare", body: ["Choose one concept your audience can investigate in a single session. Start with a simple question such as how the brain sends signals or how an interface can respond to human input."], list: ["A computer with a modern web browser", "A screen or projector for group delivery", "One facilitator and one support student", "The NeuroBridge live demo or a local copy from GitHub"] },
        { title: "Run the activity", body: ["Begin with the human question before introducing the technology. Let participants predict what will happen, try the interaction, then connect their observation to the science."], steps: ["Ask what the brain needs to communicate with a machine.", "Demonstrate one NeuroBridge interaction without technical vocabulary.", "Invite learners to test it and record what changes.", "Explain the signal, interface and response as three connected parts.", "Let small groups propose a new accessible use for the same idea."] },
        { title: "Adapt it", body: ["For younger groups, use drawings and physical role-play to represent signals. For advanced learners, inspect the source code and change one interaction. When devices are limited, run the experience as a facilitator-led demonstration."], note: "Do not present a classroom demonstration as a medical diagnostic tool. Keep personal health data out of the activity." },
        { title: "Measure impact", body: ["Collect evidence that the project improved understanding and invited participation."], list: ["Ask learners to explain the signal–interface–response chain in their own words", "Record how many participants tested or modified an interaction", "Gather one accessibility improvement from each group", "Write down changes before running the next session"] }
      ]
    },
    {
      id: "e-parenting-4-stem",
      index: "02",
      title: "E-Parenting 4 STEM",
      kicker: "Families · STEM confidence",
      status: "available",
      audience: "Parents and caregivers",
      duration: "60–90 minute workshop",
      level: "No STEM experience needed",
      tags: ["Parents", "Home activities", "Guidance"],
      summary: "Give parents the confidence and practical tools to support a child’s curiosity in STEM at home.",
      intro: "Parents do not need to be engineers to raise young engineers. E-Parenting 4 STEM helps caregivers turn everyday questions into safe, low-cost opportunities for discovery.",
      sections: [
        { title: "Purpose", body: ["Build parent confidence and make STEM support feel possible in ordinary home life."], list: ["Replace the pressure to know every answer with a habit of investigating together", "Offer activities that use familiar, affordable materials", "Help adults notice and encourage a child’s interests"] },
        { title: "Prepare", body: ["Invite parents and children together when possible. Select two short activities suited to the ages in the room and test them before the workshop."], list: ["A safe room with tables", "Everyday craft and household materials", "Printed activity prompts", "One facilitator for every 10–15 participants"] },
        { title: "Run the workshop", body: ["Model curiosity rather than expertise. The facilitator’s role is to ask useful questions and show families how to learn together."], steps: ["Open with a familiar object and ask how participants think it works.", "Introduce the ask–predict–test–reflect cycle.", "Run a short family activity without giving away the result.", "Let each family change one variable and compare outcomes.", "Close by planning one small STEM moment they can repeat at home."] },
        { title: "Adapt it", body: ["Translate activity cards into the languages used by local families. Replace hard-to-find materials with local equivalents. For an online session, provide the material list several days in advance."], note: "Review every home activity for age-appropriate supervision, allergies, heat, sharp objects and electrical risks." },
        { title: "Measure impact", body: ["Use a short before-and-after confidence prompt rather than testing technical knowledge."], list: ["Can the parent name one way to respond when they do not know an answer?", "Did each family complete or adapt an activity?", "What activity will they try next?", "Which material or instruction was difficult to access?"] }
      ]
    },
    {
      id: "arduino-experiments",
      index: "03",
      title: "Arduino Experiments",
      kicker: "Electronics · Coding",
      status: "available",
      audience: "Students aged 12+",
      duration: "19 standalone lessons",
      level: "Beginner to intermediate",
      tags: ["Arduino Uno", "Sensors", "C++"],
      summary: "Learn electronics and physical computing through 19 practical Arduino Uno experiments.",
      intro: "Start with a blinking LED, then progress through inputs, sensors, motors, automation and small robots. Every lesson includes a material list, safe wiring notes, working code and troubleshooting guidance.",
      isArduino: true,
      sections: [
        { title: "Before you begin", body: ["Install the Arduino IDE, connect an Arduino Uno with a data-capable USB cable, and select the correct board and port. Complete the experiments in order if this is your first time working with electronics."], list: ["Disconnect power before changing wiring", "Use a resistor with every standard LED", "Keep a common ground when using an external motor or fan supply", "Never power motors directly from an Arduino I/O pin"] },
        { title: "Teaching format", body: ["Each experiment works as a 30–90 minute lesson. Ask learners to predict the result, build the circuit with power disconnected, inspect each other’s wiring, upload the code and change one variable."], note: "The English web lessons correct obvious inconsistencies in the original source files. The original Turkish PDFs remain available for reference." }
      ]
    },
    {
      id: "lego-mri",
      index: "04",
      title: "LEGO MRI",
      kicker: "Health · Child-centred design",
      status: "available",
      audience: "Children, families and clinics",
      duration: "45–60 minute session",
      level: "Facilitator-led",
      tags: ["LEGO", "Medical outreach", "Children"],
      summary: "Use a familiar LEGO model to help children understand what happens during an MRI scan.",
      intro: "The LEGO MRI project turns an unfamiliar medical machine into something children can explore through play. Teams can use a model and a simple story to explain the process before a real scan.",
      sections: [
        { title: "Purpose", body: ["Reduce uncertainty by helping children become familiar with the shape, sequence and sounds of an MRI experience."], list: ["Explain the scan in concrete, age-appropriate steps", "Give children a safe way to ask questions", "Support, but never replace, guidance from healthcare professionals"] },
        { title: "Prepare", body: ["Build or obtain a LEGO model that clearly shows the scanner, moving bed and control area. Review every statement with the participating healthcare provider before delivering the activity."], list: ["LEGO MRI model with a movable patient bed", "A minifigure or small character", "A short, clinic-approved visual sequence", "A quiet table and a trained facilitator"] },
        { title: "Run the activity", body: ["Follow the same order a child will experience at the clinic, using the model to make each stage visible."], steps: ["Invite the child to explore the model and name what they notice.", "Move the character onto the bed and explain why staying still matters.", "Slide the bed into the model scanner and describe the sounds without imitating them too loudly.", "Show where the family and medical team may be during the scan.", "Let the child repeat the sequence and ask questions."] },
        { title: "Adapt it", body: ["Use the exact procedure, vocabulary and accessibility supports approved by the local clinic. Offer a visual-only version, additional processing time or a quieter one-to-one session when appropriate."], note: "This is a familiarisation activity, not medical advice. A healthcare professional must confirm local scan procedures and answer clinical questions." },
        { title: "Measure impact", body: ["Use observation and simple child-friendly questions; participation must always be voluntary."], list: ["Can the child place the model steps in order?", "Can they name one thing they expect to see or hear?", "What question do they still have?", "Ask caregivers and clinical staff which explanation helped most"] }
      ]
    },
    {
      id: "cybersecurity",
      index: "05",
      title: "Cybersecurity",
      kicker: "Digital safety · Awareness",
      status: "available",
      audience: "Students aged 11+",
      duration: "60–75 minute workshop",
      level: "Beginner",
      tags: ["Security", "Digital literacy", "Online safety"],
      summary: "Learn practical habits for protecting accounts, devices and personal information online.",
      intro: "This workshop introduces everyday cybersecurity through familiar situations: passwords, social media, suspicious messages, malware, public networks and cyberbullying.",
      sourceLinks: [
        { label: "Open the original Turkish presentation", url: "assets/resources/cybersecurity/cybersecurity-presentation-tr.pdf" }
      ],
      sections: [
        {
          title: "Purpose",
          body: ["Cybersecurity means protecting devices, accounts, personal information and digital activity from misuse. This workshop helps learners recognise common risks and choose safer actions."],
          list: ["Create stronger, unique account passwords", "Recognise suspicious messages, links and downloads", "Protect personal information on social platforms", "Know how to respond to malware and cyberbullying"]
        },
        {
          title: "Prepare",
          body: ["Review the presentation before the session and choose examples that fit your learners’ age and local context. Do not use real passwords, private messages or personal incidents as demonstration material."],
          list: ["The provided presentation and a projector", "Printed or digital scenario cards", "A board for collecting safe-action ideas", "One facilitator and a trusted safeguarding contact"]
        },
        {
          title: "Core safety habits",
          body: ["Focus on a small group of actions learners can repeat after the workshop."],
          list: ["Use a long, unique password for every important account; use a reputable password manager where appropriate", "Turn on multi-factor authentication when it is available", "Keep operating systems, browsers and security software updated", "Check the sender and web address before opening a link or attachment", "Limit personal information shared publicly and review account privacy settings", "Avoid sensitive activity on untrusted public Wi-Fi; prefer secure HTTPS connections", "Back up important files and know how to restore them"]
        },
        {
          title: "Run the workshop",
          body: ["Present each threat through a short decision rather than a long definition. Learners should practise deciding what to do next."],
          steps: ["Ask learners what they already do to protect a device or account.", "Introduce passwords, privacy and suspicious links with examples that contain no real personal data.", "Explain phishing, spyware, trojans, man-in-the-middle attacks and clickjacking in simple terms.", "Give groups scenario cards and ask them to identify the warning signs and safest response.", "Discuss cyberbullying: save evidence, block the account, report the behaviour and tell a trusted adult or responsible authority.", "Finish with each learner choosing three safety habits to apply this week."]
        },
        {
          title: "Discussion scenarios",
          body: ["Use fictional examples. Reveal the warning signs only after groups have discussed their response."],
          list: ["A message says your account will close today unless you sign in through its link", "A free game download asks you to disable antivirus protection", "A public profile reveals a student’s school, daily route and live location", "A café Wi-Fi network has a name similar to the official network but no password", "A classmate receives repeated threatening messages in a group chat"]
        },
        {
          title: "Respond safely",
          body: ["If a learner thinks an account or device has been compromised, they should stop interacting with the suspicious content and ask a trusted adult or technical lead for help."],
          list: ["Use a known-safe device to change the affected password", "Sign out other sessions and enable multi-factor authentication", "Update and scan the device with trusted security tools", "Contact the real service through its official website or app", "Preserve evidence of fraud, threats or bullying before blocking and reporting"],
          note: "Never ask learners to disclose passwords, private conversations or traumatic experiences. Follow your organisation’s safeguarding and incident-reporting process."
        },
        {
          title: "Measure learning",
          body: ["Use the same short scenarios before and after the workshop, then compare how learners explain their choices."],
          list: ["Can learners identify at least two warning signs in a suspicious message?", "Can they explain why password reuse increases risk?", "Can they name a safe response to cyberbullying?", "Can each learner choose three realistic actions for their own digital safety?"]
        }
      ]
    },
    {
      id: "technology-addiction",
      index: "06",
      title: "Technology Addiction",
      kicker: "Digital wellbeing · Coming soon",
      status: "coming",
      audience: "Students and families",
      duration: "To be announced",
      level: "To be announced",
      tags: ["Wellbeing", "Awareness"],
      summary: "A discussion-based workshop about healthy technology habits is being prepared.",
      intro: "The source presentation will be added here and converted into an accessible, reusable workshop guide."
    }
  ];

  const experiments = [
    {
      id: 1, title: "Blink an LED", level: "Beginner", time: "30 min", concept: "Digital output",
      summary: "Build your first Arduino circuit and make an LED blink once per second.",
      materials: ["Arduino Uno", "1 LED", "220 Ω resistor", "Breadboard", "Jumper wires", "USB data cable"],
      wiring: ["Disconnect USB power before wiring.", "Connect digital pin 13 to a 220 Ω resistor.", "Connect the resistor to the LED’s long leg (anode).", "Connect the LED’s short leg (cathode) to GND."],
      code: `const int ledPin = 13;\n\nvoid setup() {\n  pinMode(ledPin, OUTPUT);\n}\n\nvoid loop() {\n  digitalWrite(ledPin, HIGH);\n  delay(1000);\n  digitalWrite(ledPin, LOW);\n  delay(1000);\n}`,
      result: "The LED turns on for one second and off for one second repeatedly.", challenge: "Change both delay values to create a faster or uneven rhythm."
    },
    {
      id: 2, title: "Traffic Light", level: "Beginner", time: "40 min", concept: "Sequences",
      summary: "Control three LEDs in a timed red, yellow and green traffic-light sequence.",
      materials: ["Arduino Uno", "Red, yellow and green LEDs", "3 × 220 Ω resistors", "Breadboard", "Jumper wires", "USB data cable"],
      wiring: ["Connect pins 10, 11 and 12 through separate 220 Ω resistors to the red, yellow and green LED anodes.", "Connect all three LED cathodes to GND."],
      code: `const int red = 10;\nconst int yellow = 11;\nconst int green = 12;\n\nvoid setup() {\n  pinMode(red, OUTPUT);\n  pinMode(yellow, OUTPUT);\n  pinMode(green, OUTPUT);\n}\n\nvoid loop() {\n  digitalWrite(red, HIGH); delay(3000); digitalWrite(red, LOW);\n  digitalWrite(green, HIGH); delay(3000); digitalWrite(green, LOW);\n  digitalWrite(yellow, HIGH); delay(1000); digitalWrite(yellow, LOW);\n}`,
      result: "Only one LED is on at a time, following a repeating traffic-light sequence.", challenge: "Add a short red-and-yellow phase before green."
    },
    {
      id: 3, title: "Button-Controlled LED", level: "Beginner", time: "40 min", concept: "Digital input",
      summary: "Read a push button and use it to control an LED.",
      materials: ["Arduino Uno", "Push button", "LED", "220 Ω resistor", "10 kΩ resistor", "Breadboard and jumper wires"],
      wiring: ["Connect one side of the button to 5V and the other to pin 2.", "Connect a 10 kΩ pull-down resistor between pin 2 and GND.", "Connect pin 13 through 220 Ω to the LED anode; connect the cathode to GND."],
      code: `const int buttonPin = 2;\nconst int ledPin = 13;\n\nvoid setup() {\n  pinMode(buttonPin, INPUT);\n  pinMode(ledPin, OUTPUT);\n}\n\nvoid loop() {\n  digitalWrite(ledPin, digitalRead(buttonPin));\n}`,
      result: "The LED lights while the button is pressed.", challenge: "Change the circuit and code to use INPUT_PULLUP."
    },
    {
      id: 4, title: "LDR Light Sensor", level: "Beginner", time: "45 min", concept: "Analog input",
      summary: "Measure light with a photoresistor and switch on an LED when the room gets dark.",
      materials: ["Arduino Uno", "LDR/photoresistor", "10 kΩ resistor", "LED", "220 Ω resistor", "Breadboard and jumper wires"],
      wiring: ["Make a voltage divider: 5V → LDR → A0 → 10 kΩ → GND.", "Connect pin 13 through 220 Ω to the LED anode and its cathode to GND."],
      code: `const int ldrPin = A0;\nconst int ledPin = 13;\nconst int threshold = 400;\n\nvoid setup() {\n  pinMode(ledPin, OUTPUT);\n  Serial.begin(9600);\n}\n\nvoid loop() {\n  int light = analogRead(ldrPin);\n  Serial.println(light);\n  digitalWrite(ledPin, light < threshold ? HIGH : LOW);\n  delay(100);\n}`,
      result: "The Serial Monitor shows light readings and the LED switches on below the threshold.", challenge: "Observe your room’s values and calibrate the threshold."
    },
    {
      id: 5, title: "Sound-Activated LED", level: "Beginner", time: "40 min", concept: "Sensor input",
      summary: "Use a digital sound sensor module to flash an LED when it detects a loud sound.",
      materials: ["Arduino Uno", "Digital sound sensor module", "LED", "220 Ω resistor", "Breadboard and jumper wires"],
      wiring: ["Connect sensor VCC to 5V, GND to GND and digital OUT to pin 2.", "Connect pin 13 through 220 Ω to the LED anode; connect the cathode to GND."],
      code: `const int soundPin = 2;\nconst int ledPin = 13;\n\nvoid setup() {\n  pinMode(soundPin, INPUT);\n  pinMode(ledPin, OUTPUT);\n}\n\nvoid loop() {\n  if (digitalRead(soundPin) == HIGH) {\n    digitalWrite(ledPin, HIGH);\n    delay(200);\n  } else {\n    digitalWrite(ledPin, LOW);\n  }\n}`,
      result: "A loud sound triggers a short LED flash.", challenge: "Adjust the module potentiometer and compare sensitivity."
    },
    {
      id: 6, title: "Mix Colours with an RGB LED", level: "Beginner", time: "45 min", concept: "PWM output",
      summary: "Control the red, green and blue channels of a common-cathode RGB LED.",
      materials: ["Arduino Uno", "Common-cathode RGB LED", "3 × 220 Ω resistors", "Breadboard and jumper wires"],
      wiring: ["Connect the RGB LED common cathode to GND.", "Connect red, green and blue anodes through separate 220 Ω resistors to PWM pins 9, 10 and 11."],
      code: `const int redPin = 9, greenPin = 10, bluePin = 11;\n\nvoid colour(int r, int g, int b) {\n  analogWrite(redPin, r);\n  analogWrite(greenPin, g);\n  analogWrite(bluePin, b);\n}\n\nvoid setup() {\n  pinMode(redPin, OUTPUT); pinMode(greenPin, OUTPUT); pinMode(bluePin, OUTPUT);\n}\n\nvoid loop() {\n  colour(255, 0, 0); delay(1000);\n  colour(0, 255, 0); delay(1000);\n  colour(0, 0, 255); delay(1000);\n  colour(160, 0, 180); delay(1000);\n}`,
      result: "The LED cycles through three primary colours and purple.", challenge: "Create orange, cyan and a smooth colour fade."
    },
    {
      id: 7, title: "Moving Flag with a Servo", level: "Beginner", time: "45 min", concept: "Servo control",
      summary: "Move a lightweight paper flag between three angles with an SG90 servo.",
      materials: ["Arduino Uno", "SG90 micro servo", "Lightweight paper flag", "Jumper wires", "External regulated 5V supply recommended"],
      wiring: ["Connect servo signal to pin 9.", "Connect servo power to regulated 5V and ground to GND.", "If using an external supply, connect its GND to Arduino GND."],
      code: `#include <Servo.h>\nServo flagServo;\n\nvoid setup() {\n  flagServo.attach(9);\n}\n\nvoid loop() {\n  flagServo.write(0); delay(1000);\n  flagServo.write(90); delay(1000);\n  flagServo.write(180); delay(1000);\n}`,
      result: "The servo moves the flag between 0°, 90° and 180°.", challenge: "Use a for loop to make the motion smooth.", safety: "Do not attach a heavy object to a micro servo. Use a separate regulated supply if the servo causes the Arduino to reset."
    },
    {
      id: 8, title: "Mini Emergency Light", level: "Beginner", time: "30 min", concept: "Timed outputs",
      summary: "Alternate two coloured LEDs to create a compact warning-light pattern.",
      materials: ["Arduino Uno", "Red and blue LEDs", "2 × 220 Ω resistors", "Breadboard and jumper wires"],
      wiring: ["Connect pins 8 and 9 through separate 220 Ω resistors to the LED anodes.", "Connect both cathodes to GND."],
      code: `const int ledA = 8, ledB = 9;\n\nvoid setup() {\n  pinMode(ledA, OUTPUT); pinMode(ledB, OUTPUT);\n}\n\nvoid loop() {\n  digitalWrite(ledA, HIGH); digitalWrite(ledB, LOW); delay(150);\n  digitalWrite(ledA, LOW); digitalWrite(ledB, HIGH); delay(150);\n}`,
      result: "The two LEDs flash alternately.", challenge: "Design a double-flash pattern using a helper function."
    },
    {
      id: 9, title: "Clap-Triggered Light", level: "Beginner", time: "45 min", concept: "Event detection",
      summary: "Detect a clap or other sharp sound and light an LED briefly.",
      materials: ["Arduino Uno", "Digital microphone/sound module", "LED", "220 Ω resistor", "Breadboard and jumper wires"],
      wiring: ["Connect module VCC to 5V, GND to GND and OUT to pin 2.", "Connect pin 13 through 220 Ω to the LED anode and its cathode to GND."],
      code: `const int micPin = 2, ledPin = 13;\nunsigned long lastTrigger = 0;\n\nvoid setup() {\n  pinMode(micPin, INPUT); pinMode(ledPin, OUTPUT);\n}\n\nvoid loop() {\n  if (digitalRead(micPin) == HIGH && millis() - lastTrigger > 300) {\n    digitalWrite(ledPin, HIGH);\n    delay(200);\n    digitalWrite(ledPin, LOW);\n    lastTrigger = millis();\n  }\n}`,
      result: "A sharp sound produces one controlled flash instead of repeated triggers.", challenge: "Count claps and switch the LED state after two detections."
    },
    {
      id: 11, title: "Ultrasonic Distance Meter", level: "Intermediate", time: "55 min", concept: "Time of flight",
      summary: "Measure distance with an HC-SR04 and alert when an object comes close.",
      materials: ["Arduino Uno", "HC-SR04 ultrasonic sensor", "LED", "220 Ω resistor", "Breadboard and jumper wires"],
      wiring: ["Connect HC-SR04 VCC to 5V, GND to GND, Trig to pin 7 and Echo to pin 6.", "Connect pin 13 through 220 Ω to the LED anode and its cathode to GND."],
      code: `const int trigPin = 7, echoPin = 6, ledPin = 13;\n\nvoid setup() {\n  pinMode(trigPin, OUTPUT); pinMode(echoPin, INPUT); pinMode(ledPin, OUTPUT);\n  Serial.begin(9600);\n}\n\nvoid loop() {\n  digitalWrite(trigPin, LOW); delayMicroseconds(2);\n  digitalWrite(trigPin, HIGH); delayMicroseconds(10); digitalWrite(trigPin, LOW);\n  long duration = pulseIn(echoPin, HIGH, 30000);\n  float distance = duration * 0.0343 / 2.0;\n  Serial.println(distance);\n  digitalWrite(ledPin, duration > 0 && distance < 20 ? HIGH : LOW);\n  delay(100);\n}`,
      result: "Distance appears in centimetres and the LED turns on below 20 cm.", challenge: "Make the LED blink faster as an object gets closer."
    },
    {
      id: 12, title: "Temperature and Humidity", level: "Intermediate", time: "55 min", concept: "Digital sensor",
      summary: "Read temperature and relative humidity from a DHT11 sensor.",
      materials: ["Arduino Uno", "DHT11 module", "Jumper wires", "Arduino DHT sensor library"],
      wiring: ["Connect module VCC to 5V, GND to GND and DATA to pin 4.", "For a bare DHT11, add a 10 kΩ pull-up resistor between DATA and 5V."],
      code: `#include <DHT.h>\n#define DHTPIN 4\n#define DHTTYPE DHT11\nDHT dht(DHTPIN, DHTTYPE);\n\nvoid setup() {\n  Serial.begin(9600); dht.begin();\n}\n\nvoid loop() {\n  float humidity = dht.readHumidity();\n  float temperature = dht.readTemperature();\n  if (isnan(humidity) || isnan(temperature)) {\n    Serial.println("Sensor read failed");\n  } else {\n    Serial.print(temperature); Serial.print(" C, ");\n    Serial.print(humidity); Serial.println(" %");\n  }\n  delay(2000);\n}`,
      result: "The Serial Monitor updates temperature and humidity about every two seconds.", challenge: "Add an LED warning when temperature exceeds a chosen value."
    },
    {
      id: 13, title: "Obstacle-Avoiding Robot", level: "Intermediate", time: "90 min", concept: "Robot decisions",
      summary: "Combine a distance sensor and motor driver to make a simple robot avoid obstacles.",
      materials: ["Arduino Uno", "HC-SR04", "L298N motor driver", "2 DC gear motors and chassis", "Motor battery pack", "Jumper wires"],
      wiring: ["Connect Trig to pin 7 and Echo to pin 6.", "Connect L298N IN1–IN4 to pins 4, 5, 8 and 9; keep ENA/ENB jumpers installed.", "Power motors from the battery through the driver. Join driver and Arduino grounds."],
      code: `const int trigPin=7, echoPin=6;\nconst int in1=4, in2=5, in3=8, in4=9;\n\nvoid drive(int a, int b, int c, int d) {\n  digitalWrite(in1,a); digitalWrite(in2,b); digitalWrite(in3,c); digitalWrite(in4,d);\n}\n\nfloat distanceCm() {\n  digitalWrite(trigPin,LOW); delayMicroseconds(2);\n  digitalWrite(trigPin,HIGH); delayMicroseconds(10); digitalWrite(trigPin,LOW);\n  return pulseIn(echoPin,HIGH,30000) * 0.0343 / 2.0;\n}\n\nvoid setup() {\n  pinMode(trigPin,OUTPUT); pinMode(echoPin,INPUT);\n  pinMode(in1,OUTPUT); pinMode(in2,OUTPUT); pinMode(in3,OUTPUT); pinMode(in4,OUTPUT);\n}\n\nvoid loop() {\n  float d=distanceCm();\n  if (d > 0 && d < 20) {\n    drive(LOW,HIGH,LOW,HIGH); delay(350);\n    drive(HIGH,LOW,LOW,HIGH); delay(450);\n  } else { drive(HIGH,LOW,HIGH,LOW); }\n}`,
      result: "The robot reverses and turns when it detects an object closer than 20 cm.", challenge: "Test three thresholds and record which produces the most reliable movement.", safety: "Never power DC motors from Arduino pins or the board’s 5V regulator. Check polarity and keep moving parts clear of hair and fingers."
    },
    {
      id: 14, title: "Potentiometer LED Dimmer", level: "Beginner", time: "40 min", concept: "Analog-to-PWM mapping",
      summary: "Turn a potentiometer to control LED brightness.",
      materials: ["Arduino Uno", "10 kΩ potentiometer", "LED", "220 Ω resistor", "Breadboard and jumper wires"],
      wiring: ["Connect the potentiometer outer pins to 5V and GND; connect its centre pin to A0.", "Connect PWM pin 9 through 220 Ω to the LED anode and the cathode to GND."],
      code: `const int potPin = A0, ledPin = 9;\n\nvoid setup() { pinMode(ledPin, OUTPUT); }\n\nvoid loop() {\n  int reading = analogRead(potPin);\n  int brightness = map(reading, 0, 1023, 0, 255);\n  analogWrite(ledPin, brightness);\n}`,
      result: "LED brightness changes smoothly as the knob turns.", challenge: "Reverse the response so clockwise movement makes the LED dimmer."
    },
    {
      id: 15, title: "Single-Digit 7-Segment Display", level: "Intermediate", time: "60 min", concept: "Output arrays",
      summary: "Display the digits 0–9 on a common-cathode 7-segment display.",
      materials: ["Arduino Uno", "Common-cathode 7-segment display", "7 × 220 Ω resistors", "Breadboard and jumper wires"],
      wiring: ["Use the display datasheet to identify segments a–g and the common cathodes.", "Connect segments a–g through individual 220 Ω resistors to pins 2–8.", "Connect both common cathode pins to GND."],
      code: `const int segPins[7] = {2,3,4,5,6,7,8};\nconst byte digits[10][7] = {\n  {1,1,1,1,1,1,0},{0,1,1,0,0,0,0},{1,1,0,1,1,0,1},{1,1,1,1,0,0,1},\n  {0,1,1,0,0,1,1},{1,0,1,1,0,1,1},{1,0,1,1,1,1,1},{1,1,1,0,0,0,0},\n  {1,1,1,1,1,1,1},{1,1,1,1,0,1,1}\n};\n\nvoid showDigit(int n) {\n  for (int i=0; i<7; i++) digitalWrite(segPins[i], digits[n][i]);\n}\nvoid setup() { for (int p : segPins) pinMode(p, OUTPUT); }\nvoid loop() { for (int n=0; n<10; n++) { showDigit(n); delay(1000); } }`,
      result: "The display counts from 0 to 9 and repeats.", challenge: "Add two buttons to move the number up and down."
    },
    {
      id: 16, title: "Joystick Servo Control", level: "Intermediate", time: "50 min", concept: "Input mapping",
      summary: "Use a joystick’s horizontal axis to position a servo from 0° to 180°.",
      materials: ["Arduino Uno", "2-axis joystick module", "SG90 micro servo", "Jumper wires", "External regulated 5V supply recommended"],
      wiring: ["Connect joystick VCC to 5V, GND to GND and VRx to A0.", "Connect servo signal to pin 9 and its power to regulated 5V.", "Join external supply GND to Arduino GND."],
      code: `#include <Servo.h>\nServo arm;\nconst int joyX = A0;\n\nvoid setup() { arm.attach(9); }\n\nvoid loop() {\n  int reading = analogRead(joyX);\n  int angle = map(reading, 0, 1023, 0, 180);\n  arm.write(angle);\n  delay(15);\n}`,
      result: "The servo follows horizontal joystick movement.", challenge: "Add a small dead zone around the joystick centre to reduce jitter.", safety: "Do not force the servo horn by hand. Use a separate regulated supply if movement resets the board."
    },
    {
      id: 17, title: "Automatic Fan Controller", level: "Intermediate", time: "65 min", concept: "Threshold control",
      summary: "Switch a small DC fan on automatically when a DHT11 reports high temperature.",
      materials: ["Arduino Uno", "DHT11 module", "Logic-level N-channel MOSFET", "Small DC fan", "Flyback diode", "10 kΩ gate pull-down", "External fan supply"],
      wiring: ["Connect DHT11 DATA to pin 4.", "Drive the MOSFET gate from pin 6; add 10 kΩ from gate to GND.", "Connect fan through the MOSFET and external supply; place the diode reverse-biased across the fan.", "Join external supply and Arduino grounds."],
      code: `#include <DHT.h>\n#define DHTPIN 4\n#define DHTTYPE DHT11\nDHT dht(DHTPIN, DHTTYPE);\nconst int fanPin = 6;\nconst float threshold = 28.0;\n\nvoid setup() { pinMode(fanPin, OUTPUT); dht.begin(); }\n\nvoid loop() {\n  float temperature = dht.readTemperature();\n  if (!isnan(temperature)) digitalWrite(fanPin, temperature >= threshold);\n  delay(2000);\n}`,
      result: "The fan starts at or above 28 °C and stops below it.", challenge: "Add a second, lower off-threshold to prevent rapid switching.", safety: "Do not connect the fan directly to an Arduino output. Confirm fan voltage, diode orientation and supply polarity before powering the circuit."
    },
    {
      id: 18, title: "PIR Motion Alarm", level: "Intermediate", time: "45 min", concept: "Motion sensing",
      summary: "Detect movement with a PIR sensor and trigger a small buzzer or LED.",
      materials: ["Arduino Uno", "PIR motion sensor", "Active 5V buzzer or LED with 220 Ω resistor", "Jumper wires"],
      wiring: ["Connect PIR VCC to 5V, GND to GND and OUT to pin 2.", "Connect a low-current active buzzer to pin 8 and GND, or use an LED with a resistor."],
      code: `const int pirPin = 2, alarmPin = 8;\n\nvoid setup() {\n  pinMode(pirPin, INPUT); pinMode(alarmPin, OUTPUT);\n  Serial.begin(9600);\n}\n\nvoid loop() {\n  bool motion = digitalRead(pirPin);\n  digitalWrite(alarmPin, motion);\n  if (motion) Serial.println("Motion detected");\n  delay(100);\n}`,
      result: "After its warm-up period, the PIR activates the output when movement is detected.", challenge: "Keep the alarm active for five seconds after the last movement."
    },
    {
      id: 19, title: "Light-Following Robot", level: "Intermediate", time: "90 min", concept: "Differential control",
      summary: "Compare two light sensors and steer a two-motor robot toward the brighter side.",
      materials: ["Arduino Uno", "2 LDRs", "2 × 10 kΩ resistors", "L298N motor driver", "2 DC gear motors and chassis", "Motor battery pack"],
      wiring: ["Build two 5V LDR voltage dividers and connect their centres to A0 and A1.", "Connect L298N IN1–IN4 to pins 4–7; keep ENA/ENB jumpers installed.", "Power motors externally and join driver and Arduino grounds."],
      code: `const int leftLdr=A0, rightLdr=A1;\nconst int in1=4, in2=5, in3=6, in4=7;\n\nvoid motors(bool lf, bool lb, bool rf, bool rb) {\n  digitalWrite(in1,lf); digitalWrite(in2,lb);\n  digitalWrite(in3,rf); digitalWrite(in4,rb);\n}\nvoid setup() {\n  pinMode(in1,OUTPUT); pinMode(in2,OUTPUT); pinMode(in3,OUTPUT); pinMode(in4,OUTPUT);\n}\nvoid loop() {\n  int left=analogRead(leftLdr), right=analogRead(rightLdr);\n  int difference=left-right;\n  if (abs(difference)<50) motors(HIGH,LOW,HIGH,LOW);\n  else if (difference>0) motors(LOW,LOW,HIGH,LOW);\n  else motors(HIGH,LOW,LOW,LOW);\n}`,
      result: "The robot moves forward under balanced light and turns toward the brighter sensor.", challenge: "Calibrate the dead-band and shield the two LDRs from each other.", safety: "Power motors through the driver and a suitable battery only. Keep the robot on a clear floor and restrain it during the first powered test."
    },
    {
      id: 20, title: "Mini Digital Clock", level: "Intermediate", time: "75 min", concept: "I²C and timekeeping",
      summary: "Read time from a DS3231 real-time clock and show it on an I²C LCD.",
      materials: ["Arduino Uno", "DS3231 RTC module", "16×2 I²C LCD", "Jumper wires", "RTClib and LiquidCrystal_I2C libraries"],
      wiring: ["Connect both modules to 5V and GND.", "Connect both SDA pins to A4 and both SCL pins to A5 on the Uno.", "Check the LCD address with an I²C scanner; 0x27 is common."],
      code: `#include <Wire.h>\n#include <RTClib.h>\n#include <LiquidCrystal_I2C.h>\nRTC_DS3231 rtc;\nLiquidCrystal_I2C lcd(0x27, 16, 2);\n\nvoid setup() {\n  lcd.init(); lcd.backlight();\n  if (!rtc.begin()) { lcd.print("RTC not found"); while (true) {} }\n  // Run once if needed, then comment out and upload again:\n  // rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));\n}\n\nvoid loop() {\n  DateTime now = rtc.now();\n  lcd.setCursor(0,0);\n  if (now.hour()<10) lcd.print('0'); lcd.print(now.hour()); lcd.print(':');\n  if (now.minute()<10) lcd.print('0'); lcd.print(now.minute()); lcd.print(':');\n  if (now.second()<10) lcd.print('0'); lcd.print(now.second());\n  lcd.setCursor(0,1);\n  lcd.print(now.day()); lcd.print('/'); lcd.print(now.month()); lcd.print('/'); lcd.print(now.year());\n  delay(500);\n}`,
      result: "The LCD displays the current time and date while the RTC keeps time when unplugged.", challenge: "Add two buttons to choose between clock and temperature views."
    }
  ];

  window.LEARNING_DATA = { projects, experiments };
}());

import React, { useState, useEffect, useRef } from "react";
import io from 'socket.io-client';
import './App.css';

const socket = io('http://localhost:8000');


function App() {

  const [temp, setTemp] = useState(null);
  const [ultrasonic, setUltrasonic] = useState(null);
  const [humidity, setHumidity] = useState(null);

  const [direction, setDirection] = useState(null); // Rover movement
  const [motorPower, setMotorPower] = useState(null); // Motor power, 1-9

  const [armValue, setArmValue] = useState(null); // Rotational and vertical movement
  const [pinchValue, setPinchValue] = useState(null); // Grabbing/releasing


  const speedOfSound = .0343; // Speed of sound in cm/us
  const cameraURL = "http://esp32-tv:81/stream" // ESP32 camera URL


  useEffect(() => {

    // Listen for temperature updates
    socket.on('temp', (data) => {
      setTemp(data);
    });

    // Listen for ultrasonic updates
    socket.on('ultrasonic', (data) => {
      setUltrasonic(data);
    });

    socket.on('humidity', (data) => {
      setHumidity(data);
    });


    // Listen for keystroke input - holding key spams the server
    const handleKeyDown = (event) => {
      // Rover movement and power
      if (event.key === 'w') {
        setDirection("forward");
        sendDirection("forward");
      } else if (event.key === 'a') {
        setDirection("left");
        sendDirection("left");
      } else if (event.key === 's') {
        setDirection("back");
        sendDirection("back");
      } else if (event.key === 'd') {
        setDirection("right");
        sendDirection("right");
      } else if (event.key === ' ') { // Stops movements of Rover, Arm, and Pinch (basically a "kill movement")
        setDirection("stop");
        sendDirection("stop");
        setArmValue("stop")
        sendArmValue("stop")
        setPinchValue("stop");
        sendPinchValue("stop");
      } else if (/\d/.test(event.key)) { // Is digit?
        const newMotorPower = parseInt(event.key); // Convert string number to integer number
        if (newMotorPower >= 0 && newMotorPower <= 9) {
          const newMotorPowerString = newMotorPower.toString(); // Convert back to string
          setMotorPower(newMotorPowerString);
          sendMotorPower(newMotorPowerString);
        }
      }

      // Arm movement
      else if (event.key === 'ArrowUp') { // Rotation and height control
        setArmValue("up");
        sendArmValue("up");
      } else if (event.key === 'ArrowDown') {
        setArmValue("down");
        sendArmValue("down");
      } else if (event.key === 'ArrowLeft') {
        setArmValue("counterClockwise");
        sendArmValue("counterClockwise");
      } else if (event.key === 'ArrowRight') {
        setArmValue("clockwise");
        sendArmValue("clockwise");
      } else if (event.key === 'g') { // Pinch control
        setPinchValue("grab");
        sendPinchValue("grab");
      } else if (event.key === 'r') {
        setPinchValue("release");
        sendPinchValue("release");
      }
    }


    // What happens when key is not pressed (nothing)
    const handleKeyUp = () => {
    }

    // Key press/depress
    window.addEventListener('keydown', handleKeyDown);
    window.addEventListener('keyup', handleKeyUp)



    return () => {
      socket.off('temp');
      socket.off('ultrasonic');
      socket.off('humidity');
      window.removeEventListener('keydown', handleKeyDown);
      window.removeEventListener('keyup', handleKeyUp)
    };
  }, []);

  const distanceCm = ultrasonic // Data from ultrasonic saved as distanceCm
  
  // Sends website input data to backend
  const sendDirection = (direction) => {
    socket.emit('send-direction', direction);
  };
  
  const sendMotorPower = (motorPower) => {
    socket.emit('send-motorPower', motorPower);
  };

  const sendArmValue = (value) => {
    socket.emit('send-arm-value', value);
  };

  const sendPinchValue = (value) => {
    socket.emit('send-pinch-value', value);
  };

  
  // Webpage 
  return (
    <div className="App">
      <div className="page-title">
        <h1>Team Viper Control Center</h1>
      </div>
      
      <div className="vid-feed">
        <iframe src={cameraURL} width="640" height="480" frameborder="1"></iframe>
      </div>  

      <div className="environment-data">
        <p className="data"> Temperature: {temp}&deg;C / {temp * 9/5 + 32}&deg;F</p>
        <p className="data"> Humidity: {humidity}%</p>
        <p className="data"> Rear Distance: {distanceCm} cm</p>
      </div>
      <div className="control-display">
        <h3>Current Direction: {direction}</h3>
        <h3>Current Power: {motorPower}</h3>
        <h3>Current Arm Value: {armValue}</h3>
        <h3>Current Pinch Value: {pinchValue}</h3>
      </div>
    </div>
  );
}

export default App;
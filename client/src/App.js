import React from "react";
import { Routes, Route } from "react-router-dom";
import socketClient from "socket.io-client";
import Register from "./pages/Register.js";
import Login from "./pages/Login.js";
import Home from "./pages/Home.js";
const SERVER_URL = "http://localhost:5000";

function App() {
  var socket = socketClient(SERVER_URL);

  socket.on("connect", () => {
    console.log(`I'm connected to ${SERVER_URL}`);
  });

  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
    </Routes>
  );
}

export default App;

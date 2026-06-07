import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import LoginPage from "./components/LoginPage";
import Dashboard from "./components/Dashboard";

function App() {
  const isAuth = !!localStorage.getItem("token");
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/dashboard/*" element={isAuth ? <Dashboard /> : <Navigate to="/login" />} />
        <Route path="*" element={<Navigate to={isAuth ? "/dashboard" : "/login"} />} />
      </Routes>
    </Router>
  );
}

export default App;

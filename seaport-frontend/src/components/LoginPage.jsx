import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setError("");
    try {
      const res = await fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
      });
      const data = await res.json();
      if (res.ok) {
        localStorage.setItem("token", data.token);
        navigate("/dashboard/*");
      } else {
        setError(data.error || "Login failed");
      }
    } catch {
      setError("Server error");
    }
  };

  return (
    <div className="flex h-screen items-center justify-center bg-blue-100">
      <form className="bg-white p-8 rounded-xl shadow-xl w-full max-w-xs" onSubmit={handleLogin}>
        <h2 className="text-2xl font-bold mb-6 text-center text-blue-900">Admin Login</h2>
        <input
          className="block w-full mb-4 p-2 border border-gray-300 rounded"
          value={username}
          onChange={e=>setUsername(e.target.value)}
          placeholder="Username"
          required
        />
        <input
          type="password"
          className="block w-full mb-4 p-2 border border-gray-300 rounded"
          value={password}
          onChange={e=>setPassword(e.target.value)}
          placeholder="Password"
          required
        />
        <button className="w-full py-2 bg-blue-600 hover:bg-blue-700 text-white font-semibold rounded">
          Login
        </button>
        {error && <div className="text-red-600 text-center mt-2">{error}</div>}
      </form>
    
    </div>
  );
}

import React, { useState } from "react";
import Sidebar from "./Sidebar";
import { useNavigate } from "react-router-dom";

export default function Dashboard() {
  const [section, setSection] = useState("Dashboard");
  const navigate = useNavigate();

  const handleSidebar = (item) => {
    if(item === "Logout") {
      localStorage.removeItem("token");
      navigate("/login");
    } else {
      setSection(item);
    }
  };

  return (
    <div className="flex h-screen bg-blue-50">
      <Sidebar onSelect={handleSidebar} />
      <main className="flex-1 p-12">
        <h1 className="text-2xl font-bold mb-4">{section}</h1>
        <p className="text-gray-700">
          {section === "Dashboard"
            ? "Welcome to the Admin Dashboard! Select a section from the sidebar."
            : `You are viewing: ${section}`}
        </p>
      </main>
    </div>
  );
}

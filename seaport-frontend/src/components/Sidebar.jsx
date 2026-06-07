import React from "react";

const sidebarItems = [
  "Dashboard", "Manage Users", "Documents", "Shipments", "Containers", "Payments",
  "Tracking", "Yard Management", "Reports", "Notifications", "Support/Chat", "Settings", "Logout"
];

export default function Sidebar({ onSelect }) {
  return (
    <aside className="w-56 bg-blue-800 text-white min-h-screen p-6">
      <div className="font-bold text-xl mb-8 text-center">Admin Panel</div>
      {sidebarItems.map(item => (
        <div
          key={item}
          onClick={() => onSelect(item)}
          className="py-2 px-4 my-2 rounded hover:bg-blue-700 cursor-pointer"
        >
          {item}
        </div>
      ))}
    </aside>
  );
}

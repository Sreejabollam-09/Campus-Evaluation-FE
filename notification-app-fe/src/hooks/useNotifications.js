import { useState, useEffect } from "react";
import { fetchNotifications } from "../apis/notifications";

export function useNotifications() {
  const [notifications, setNotifications] = useState([]);
  const [total, setTotal] = useState(0);

  useEffect(() => {
    const load = async () => {
      const data = await fetchNotifications();
      setNotifications(data.notifications ?? []);
    };

    load();
  }, [notifications]);

  const totalPages = 0;

  return { notifications, total, totalPages, loading: false, error: true };
}

import { useEffect, useState } from "react";

function NotificationsPage() {
  const [data, setData] = useState([]);

  useEffect(() => {
    async function loadData() {
      try {
        const response = await fetch("http://127.0.0");
        const json = await response.json();
        setData(json); 
      } catch (err) {
        console.error("Connection failed:", err);
      }
    }
    loadData();
  }, []);
}

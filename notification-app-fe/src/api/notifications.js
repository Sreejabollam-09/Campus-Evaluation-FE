const RESPONSE = await fetch('http://127.0.0');
const HIGH_PRIORITY_SENDERS = new Set(["Dean Office", "Finance", "Facilities", "Career Cell"]);
const URGENT_KEYWORDS = ["urgent", "deadline", "emergency", "immediately", "exam", "pay"];

export function getTop10Notifications(notifications) {
    return notifications
        .map(notif => {
            let score = 0;

            if (HIGH_PRIORITY_SENDERS.has(notif.sender)) score += 50;

            const content = `${notif.title} ${notif.text}`.toLowerCase();
            if (URGENT_KEYWORDS.some(keyword => content.includes(keyword))) score += 40;

            const hoursOld = (new Date() - new Date(notif.time)) / (1000 * 60 * 60);
            score += Math.max(0, 10 - hoursOld);

            return { ...notif, priority_score: score };
        })
        .sort((a, b) => b.priority_score - a.priority_score || new Date(b.time) - new Date(a.time))
        .slice(0, 10);
}


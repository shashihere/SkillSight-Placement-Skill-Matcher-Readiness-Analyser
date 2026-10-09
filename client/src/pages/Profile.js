import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

export default function Profile() {
  const navigate = useNavigate();
  const [user, setUser] = useState({ name: "", email: "" });

  useEffect(() => {
    const userData = localStorage.getItem("user");
    if (!userData) {
      navigate("/login");
    } else {
      setUser(JSON.parse(userData));
    }
  }, [navigate]);

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    navigate("/login");
  };

  return (
    <div style={styles.page}>
      <div style={styles.navbar}>
        <h2 style={styles.logo}>SkillSight</h2>
        <div style={styles.navBtns}>
          <button style={styles.backBtn} onClick={() => navigate("/CareerDashboard")}>Dashboard</button>
          <button style={styles.logoutBtn} onClick={handleLogout}>Logout</button>
        </div>
      </div>

      <div style={styles.container}>
        <div style={styles.card}>
          <div style={styles.avatar}>👤</div>
          <h1 style={styles.name}>{user.name}</h1>
          <p style={styles.email}>{user.email}</p>
        </div>
      </div>
    </div>
  );
}

const styles = {
  page: {
    minHeight: "100vh",
    background: "#edf3ff",
    fontFamily: "Arial"
  },
  navbar: {
    height: "80px",
    background: "#ffffff",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    padding: "0 30px",
    boxShadow: "0 4px 15px rgba(0,0,0,0.06)"
  },
  logo: {
    margin: 0,
    fontSize: "32px",
    fontWeight: "700",
    color: "#111827"
  },
  navBtns: {
    display: "flex"
  },
  backBtn: {
    padding: "10px 24px",
    borderRadius: "30px",
    border: "none",
    background: "#111827",
    color: "#ffffff",
    fontWeight: "700",
    fontSize: "16px",
    cursor: "pointer",
    marginRight: "10px"
  },
  logoutBtn: {
    padding: "10px 24px",
    borderRadius: "30px",
    border: "none",
    background: "#ef4444",
    color: "#ffffff",
    fontWeight: "700",
    fontSize: "16px",
    cursor: "pointer"
  },
  container: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    paddingTop: "100px"
  },
  card: {
    background: "#ffffff",
    padding: "40px",
    borderRadius: "22px",
    boxShadow: "0 12px 28px rgba(37,99,235,0.10)",
    textAlign: "center",
    width: "350px"
  },
  avatar: {
    fontSize: "60px",
    marginBottom: "20px"
  },
  name: {
    fontSize: "28px",
    fontWeight: "700",
    color: "#0f172a",
    margin: "0 0 10px 0"
  },
  email: {
    fontSize: "18px",
    color: "#475569",
    margin: "0"
  }
};

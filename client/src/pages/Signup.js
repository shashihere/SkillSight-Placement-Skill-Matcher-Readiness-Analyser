import { useState, useEffect } from "react";
import { useNavigate, Link } from "react-router-dom";
import img from "../assets/login.png";
import "./Login.css";

export default function Signup() {

  const [form, setForm] = useState({
    name: "",
    email: "",
    password: ""
  });

  const navigate = useNavigate();
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    const saved = localStorage.getItem("theme");
    if (saved === "dark") {
      setDarkMode(true);
      document.body.classList.add("dark");
    }
  }, []);

  const toggleTheme = () => {
    if (darkMode) {
      document.body.classList.remove("dark");
      localStorage.setItem("theme", "light");
      setDarkMode(false);
    } else {
      document.body.classList.add("dark");
      localStorage.setItem("theme", "dark");
      setDarkMode(true);
    }
  };

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSignup = async () => {
    if (!form.name || !form.email || !form.password) {
      alert("Please fill all fields");
      return;
    }

    try {
      const res = await fetch("http://127.0.0.1:5000/api/auth/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form)
      });
      const data = await res.json();
      
      if (res.ok) {
        localStorage.setItem("token", data.token);
        localStorage.setItem("user", JSON.stringify({ name: data.name, email: data.email }));
        navigate("/success");
      } else {
        alert(data.error || "Registration failed");
      }
    } catch (err) {
      alert("Network error");
    }
  };

  return (
    <div className="login-page">
      <button className="theme-btn" onClick={toggleTheme}>
        {darkMode ? "☀ Light Mode" : "🌙 Dark Mode"}
      </button>

      <div className="left">
        <div className="card">
          <h1>SkillSight AI</h1>
          <p className="sub">AI Powered Placement Readiness Analyzer</p>

          <div className="features">
            <p>✔ Create an Account</p>
            <p>✔ Analyze your Resume</p>
          </div>

          <div className="divider"></div>

          <input type="text" name="name" placeholder="Full Name" onChange={handleChange}/>
          <input type="email" name="email" placeholder="Email Address" onChange={handleChange}/>
          <input type="password" name="password" placeholder="Password" onChange={handleChange}/>

          <button onClick={handleSignup}>Sign Up 🚀</button>
          
          <p style={{marginTop: "15px"}}>
            Already have an account? <Link to="/login">Login here</Link>
          </p>
        </div>
      </div>

      <div className="right">
        <img src={img} alt="AI" />
      </div>
    </div>
  );
}

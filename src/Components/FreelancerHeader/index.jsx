import React from "react";
import "./index.css";
import { Link } from "react-router-dom";

const FreelancerHeader = () => {
  return (
    <header>
      <div className="topNav">
        <div className="logo">
          <h1>
            <Link to="/" style={{ color: "#222" }}>
              Flance
            </Link>
          </h1>
        </div>
        <nav>
          <ul>
            <li>
              <i class="fas fa-bell"></i>
              Notification
            </li>
            <li>
              <i class="fas fa-comment-alt"></i>
              Messages
            </li>
            <li id="Profiledropdown">
              <div className="displayPicture"></div>
              NAME
              <i class="fas fa-caret-down"></i>
            </li>
          </ul>
        </nav>
      </div>
      <div className="bottomNav">
        <div className="navLeft">
          <ul>
            <li>Projects</li>
            <li>Dashboard</li>
            <li>Post a Project</li>
          </ul>
        </div>
        <div className="navRight">
          <ul>
            <li>
              <i class="fas fa-search"></i>
              Search
            </li>
          </ul>
        </div>
      </div>
    </header>
  );
};

export default FreelancerHeader;

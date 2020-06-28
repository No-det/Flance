import React from "react";
import "./index.css";
import { Link } from "react-router-dom";

const FreelancerHeader = () => {
  function handleHamburgerClick() {
    document.querySelector(".mobileNav").style.width = "200px";
  }
  const handleNavClose = () => {
    document.querySelector(".mobileNav").style.width = "0px";
  };
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
              <p>Notification</p>
            </li>
            <hr />
            <li>
              <i class="fas fa-comment-alt"></i>
              <p>Messages</p>
            </li>
            <li id="Profiledropdown">
              <div className="displayPicture"></div>
              <p>NAME</p>
              <i class="fas fa-caret-down"></i>
            </li>
          </ul>
        </nav>
        <div className="mobileNavWrapper">
          <div className="hamburger" onClick={handleHamburgerClick}>
            <i class="fas fa-bars fa-2x"></i>
          </div>
          <div className="mobileNav">
            <i class="fas fa-times fa-2x" onClick={handleNavClose}></i>
            <ul>
              <li>
                <div className="displayPicture"></div>
                <p>NAME</p>
              </li>
              <li>
                <i class="fas fa-bell"></i>
                <p>Notification</p>
              </li>
              <li>
                <i class="fas fa-comment-alt"></i>
                <p>Messages</p>
              </li>
              <li>
                <i class="fas fa-cog"></i>
                <p>Settings</p>
              </li>
            </ul>
          </div>
        </div>
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

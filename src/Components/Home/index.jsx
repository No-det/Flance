import React from "react";
import { Button } from "antd";
import "./index.css";
import Image from "./Assets/freelance.svg";

const Home = () => {
  return (
    <div className="mainDiv">
      <div className="header">
        <div className="brandName">FLANCE</div>
        <div className="headerBtnContainer">
          <div type="default" className="headerBtn">
            Home
          </div>
          <div type="default" className="headerBtn">
            Services
          </div>
          <div type="default" className="headerBtn">
            About
          </div>
          <div type="default" className="headerBtn loginBtn">
            Login
          </div>
        </div>
      </div>
      <div className="content">
        <div className="landingLeft">
          <div className="taglinePrimary">
            <h1>Hire the best in Class</h1>
          </div>
          <div className="taglineSecondary">
            <h2>Turn your ideas into reality</h2>
          </div>
          <div className="landingMainBtn">
            <Button type="default" className="mainBtn">
              Hire a freelancer
            </Button>
            <Button type="default" className="mainBtn">
              Start freelancing today
            </Button>
          </div>
        </div>
        <div className="landingRight">
          <img src={Image} alt="svgImage" />
        </div>
      </div>
    </div>
  );
};

export default Home;

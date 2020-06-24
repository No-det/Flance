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
          <Button type="default" className="headerBtn">
            Home
          </Button>
          <Button type="default" className="headerBtn">
            Services
          </Button>
          <Button type="default" className="headerBtn">
            About
          </Button>
          <Button type="default" className="headerBtn">
            Login
          </Button>
        </div>
      </div>
      <div className="content">
        <div>
          <div style={{ fontSize: "xx-large", fontWeight: "bolder" }}>
            <h1>Hire the best in Class</h1>
          </div>
          <div style={{ fontSize: "medium", fontWeight: "bolder" }}>
            <h2>Turn your ideas into reality</h2>
          </div>
          <div
            style={{
              display: "flex",
              alignItems: "center",
              justifyContent: "flex-start",
              flexDirection: "row",
            }}
          >
            <Button type="default" className="mainBtn">
              Hire a freelancer
            </Button>
            <Button type="default" className="mainBtn">
              Start freelancing today
            </Button>
          </div>
        </div>
        <div style={{ marginLeft: 200 }}>
          <img src={Image} alt="svgImage" />
        </div>
      </div>
    </div>
  );
};

export default Home;

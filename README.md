# AWS DeepRacer Runner-Up Configuration 🎖️

This repository contains the **training configuration** that helped us secure the **runner-up position** in an AWS DeepRacer Time Trial competition.

---

## 🏁 Race Details

- **Race Type:** Time Trial  
- **Environment Simulation:** re:Invent 2018 – Counterclockwise  
- **Sensor(s):** Camera  
- **Action Space Type:** Continuous  
- **Action Space:**  
  - Speed: `[0.7 – 3.2] m/s`  
  - Steering Angle: `[-28.9° – 28.9°]`  
- **Framework:** TensorFlow  
- **Reinforcement Learning Algorithm:** PPO  

---

## ⚙️ Training Hyperparameters

| Parameter | Value |
|-----------|-------|
| Gradient Descent Batch Size | 64 |
| Entropy | 0.01 |
| Discount Factor | 0.95 |
| Loss Type | Huber |
| Learning Rate | 0.0005 |
| Experience Episodes Between Policy Update | 32 |
| Number of Epochs | 10 |

---

## 🏆 Evaluation Results

| Trial | Time (MM:SS.mmm) | Track Completed | Status | Off-Track | Crashes |
|-------|-----------------|----------------|--------|------------|---------|
| 1 | 00:12.530 | 100% | Lap Complete | 0 | 0 |
| 2 | 00:11.673 | 100% | Lap Complete | 0 | 0 |
| 3 | 00:12.134 | 100% | Lap Complete | 0 | 0 |

---

## 🔑 Key Takeaways

- **Continuous Action Space + PPO** provided smooth control for speed and steering.  
- Proper **reward shaping** ensured alignment with the track, optimal speed, and lap completion efficiency.  
- Minor penalties for oversteering helped maintain stability without sacrificing speed.  

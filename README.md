# Alsvin for businesses enabling experiences

## Alsvin

From norse mythology, Alsvin, a name given to one of the horses pulling the sun across the celestial sky. When translated it means 'swift' or 'very swift'. Adopting this name to our service which relies heavily on 5G to pull video data to be processed to enable experience based storefronts. 

![Alsvin](https://www.rivervoyages.com/news/wp-content/uploads/2014/03/The_Sun_and_Moon_Arvakr_Alsvin_Svalin_Aldsvider_Hrimfaxi_Skinfaxi1.jpg)

## Introduction

With businesses shifting into a digital era, the digitization of in-store experiences has become a vital priority. Using 5G and AI we can enable businesses to understand consumer behavior as well as stock movement. Since a majority of businesses still lack a digital infrastructure (wifi enabled systems) within their storefronts. We enable this transition by focusing on an already digitally enabled product, 5G IoT Devices, such as security cameras. Turning a static storefront into a digital storefront, that attempts to shift thinking towards monetization of their data. 

This project heavily uses the 5G network and machine learning for detection of consumer behavior. Capturing video either through an IoT enabled device (Raspberry PI) or a web UI. This video can then be processed through our backend Alsvin which uses supervised and reinforcement learning techniques to establish a consumer persona. 

### Why 5G? 
* There is no reliance on cables or local wifi
* Rapid deployment of heavy intensive data digital experiences
* Increase cyber security - no reliance on a router (common vector of attack) 
* Enhances imaging and video capabilities where traditional wifi systems (<5 mbps) lead to high pixelation

## Requirements 

* 5G enabled VPC with an EC2 
* Backend Alsvin running within EC2 5G VPC to process streaming data
* Machine Learning model tested and trained within SageMaker


## Problem
* Retailers are still far behind in digitizing their storefronts and taking advantage of the data within their storefronts. This transition is difficult due to a heavy reliance on expertise of technical solutions. Even managing a wifi system is difficult. Brick & Mortar Retailers are losing customers. 

## Solution
* We created an end-to-end solution from Web UI (intially tested with an IoT camera - raspberry pi) to backend machine learning model - which examines consumer behavior - from fraud behavior to shopping behavior. This can also lead us to examine the movement of their stock. 

Traditionally this is done through an ERP system or a manual paper tracking method. Using 5G and AI we can enable retailers to enable better experiences for consumers. Such as detecting consumer personas.

## Architecture 


## References

* https://aws5gedge.devpost.com/ 
* https://d1.awsstatic.com/Wavelength2020/Wavelength-Solution-Brief-FINAL-Aug2020.pdf 
* https://copilot.github.com/ 
* https://aws.amazon.com/fraud-detector/ 
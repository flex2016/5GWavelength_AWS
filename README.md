# Alsvin for businesses enabling experiences

## Alsvin

From norse mythology, Alsvin, a name given to one of the horses pulling the sun across the celestial sky. When translated it means 'swift' or 'very swift'. Adopting this name to our service which relies heavily on 5G to pull video data to be processed to enable experience based storefronts. 

![Alsvin](https://www.rivervoyages.com/news/wp-content/uploads/2014/03/The_Sun_and_Moon_Arvakr_Alsvin_Svalin_Aldsvider_Hrimfaxi_Skinfaxi1.jpg)

## Introduction

With businesses shifting into a digital era, digitization of in store experiences has become a vital priority. Using 5G and AI we can enable businesses to understand consumer behavior as well as stock movement. Since a majority of businesses still lack a digital infrastracture (wifi enabled systems) within their store fronts. We enable this transition by focusing on an already digitally enabled product, 5G Iot Devices, such as security cameras. Turning a static store front into a digital store front, that attempts to shift thinking towards monetization of their data. 

This project heavily uses the 5G network and machine learning for detection of consumer behavior

With businesses moving online, fraud and abuse in online systems is constantly increasing as well. Traditionally, rule-based fraud detection systems are used to combat online fraud, but these rely on a static set of rules created by human experts. This project uses machine learning to create models for fraud detection that are dynamic, self-improving and maintainable. Importantly, they can scale with the online business.

Specifically, we show how to use Amazon SageMaker to train supervised and unsupervised machine learning models on historical transactions, so that they can predict the likelihood of incoming transactions being fraudulent or not. We also show how to deploy the models, once trained, to a REST API that can be integrated into an existing business software infrastructure. This project includes a demonstration of this process using a public, anonymized credit card transactions dataset provided by ULB, but can be easily modified to work with custom labelled or unlaballed data provided as a relational table in csv format.

### Why 5G? 
* There is no reliance on cables or local wifi
* Increase cyber security - no reliance on a router (common vector of attack) 
* Enhances imaging and video capabilities where traditional wifi systems (<5 mbps) lead to high pixelation

## Requirements 

* 5G enabled VPC with an EC2 
* Backend Alsvin running within EC2 5G VPC to process streaming data
* Machine Learning model tested and trained within SageMaker


## Problem
* Retailers are still far behind in digitizing their storefronts and taking advantage of the data within their storefronts. This transition is difficult due to a heavy reliance on expertise of technical solutions. Even managing a wifi system is difficult. 

## Solution
* We created an end-to-end solution from Web UI (intially tested with an IoT camera - raspberry pi) to backend machine learning model - which examines consumer behavior - from fraud behavior to shopping behavior. This can also lead us to examine the movement of their stock. 

Traditionally this is done through an ERP system or a manual paper tracking method. Using 5G and AI we can enable retailers to enable better experiences for consumers. 

## Architecture 


## References

* https://aws5gedge.devpost.com/ 
* https://d1.awsstatic.com/Wavelength2020/Wavelength-Solution-Brief-FINAL-Aug2020.pdf 
* https://copilot.github.com/ 
* https://aws.amazon.com/fraud-detector/ 
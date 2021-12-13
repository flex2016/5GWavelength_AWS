## Inspiration
Both of us come from the eCommerce space as well as the retail space - we see the disconnection between offline and online experiences. We're heavily involved with retail experiences. Vlad recently traveled to Germany where there was a significant emphasis on "experiences" - visiting the JBL (Harman audio) flagship store. The products themselves weren't the center point as is traditionally the case. Instead, there was a heavy emphasis on the experience of the brand itself. A majority of businesses in America to this day approach retail from a product view instead of a data view. However many of these stores (Germany included) to this day are still disconnected digitally (no wifi systems in place).

With 5G and AI we can **enable businesses to view their storefronts as a data engine**. Being a partner in enabling them to become truly digital within the confines of a brick and mortar location. 

### Why 5G? 
* There is no reliance on cables or local wifi - usually requiring technical expertise
* Rapid deployment of heavy intensive data digital experiences
* Increase cyber security - no reliance on a router (common vector of attack) 
* Enhances imaging and video capabilities where traditional wifi systems (<5 Mbps) lead to high pixelation


## What it does
5G and AI can have a profound impact on SBA-designated Small Businesses. We can stream video data from security and IoT devices. And process this data to figure out consumer behavior as well as stock movement. We attempt to build a buyer persona based on video data. Since losing a customer is costly.

## How we built it
* Demo raspberry pi with a camera module
* React UI (for capturing demo video)
* 5G VPC enabled EC2
* An end to end architecture design for a 5G enabled service
* AWS SageMaker
* ML model for detecting buyer personas based on video data 

## Challenges we ran into
* Pulling data from the actual vendor themselves (unless we partner), however, we can pull data from locations that do choose to install our app that can pull the data feed directly from the router itself, and encourage small businesses to adopt a 5G approach to video security
* Streaming data on an open connection versus saving as chunks and blobs - we had to process video data from our phones and UI 
* Figuring out which streaming service to use within Amazon - given that there are so many options depending on use case - we experimented with kinesis data streams and kinesis firehose.
* We were hoping to demo a use case of stock movement but ran into significant issues demonstrating how the stock could shift in a time series scenario. 


## Accomplishments that we're proud of
* Built out a prototype raspberry pi for capturing video
* WebUI to simulate a video capturing of an IoT device
* 5G VPC networked EC2 to run Alsvin (our backend)
* Machine Learning Model that can use video to detect consumer behavior - willingness to spend

## What we learned
* The true power of 5G comes from the rapid deployment of solution-enabled IoT devices to locations that are ready to digitize. With 5G we remove traditional vectors of cyber security attacks. There isn't a reliance on a technical expert - the 5G solution simply works out of the box. And with the power of the 5G network, video and images come in consistently. 

## What's next for 
* Partner with a 5G security camera IoT provider 
* Partner with 5G enabled retailers
* Continue training machine learning model from partnered businesses that take advantage of 5G security
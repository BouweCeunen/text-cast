# Textcast - Text messages on screen

Textcast will allow you to view textmessages directly on your computer screen. It uses the Textcast app along with the software to run on your computer. The Android application broadcasts your text messages over UDP in your network over a specific port which in turn will be received by the software running on your computer. 

Feel free to let me know if something isn't working as it should at bouwe.ceunen@gmail.com

### Things to consider
- Your phone and computer must be connected to the same network through wifi or ethernet when your text message arrives.
- Make sure there are no firewall restrictions on incoming UDP messages.

### Get it running (macOS, Windows, Linux)

Run this command in your terminal of choice.
```sh
$ python textmessage.py 4090
```
This will run the python script along with port 4090, which is the same port specified on the Textcast app (can be changed), to listen on UDP broadcast messages in a specific format. This port has to be the same on your Textcast app in order to work. Note that anyone in your network UDP listening on that specific port will also get the text messages.

### Textcast app

The Textcast app is needed to broadcast your textmessages over the network as soon as they come in. This app is available on 

https://play.google.com/store/apps/details?id=com.bouweceunen.textcast

[![](http://www.bouweceunen.com/textcast/textcast.png)](http://www.bouweceunen.com/textcast/textcast.png)

### macOS preview
[![](http://www.bouweceunen.com/textcast/macOS.png)](http://www.bouweceunen.com/textcast/macOS.png)
### Windows preview
[![](http://www.bouweceunen.com/textcast/windows.png)](http://www.bouweceunen.com/textcast/windows.png)
### Linux preview
 [![](http://www.bouweceunen.com/textcast/linux.png)](http://www.bouweceunen.com/textcast/linux.png)

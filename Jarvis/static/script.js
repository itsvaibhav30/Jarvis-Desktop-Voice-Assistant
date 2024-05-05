

document.getElementById('recordButton').addEventListener('click', function() {
  recordVoice();
});

async function recordVoice() {
  try {
      console.log("listening")
      const recognition = new webkitSpeechRecognition() //|| new SpeechRecognition();
      recognition.lang = 'en-us';
      recognition.start();
    
        recognition.onresult = async (event) => {
            const voice_command = event.results[0][0].transcript;
            console.log('Voice command:', voice_command);
            console.log("listening stopped")

        // Check if the voice command is to play music
        // if (voice_command.includes('play music')) {
        //     // Replace '/path/to/your/music.mp3' with the actual path to your music file
        //     playMusic("C:\\Users\\vaibh\\Music\\UnakkuThaan.mp3");
        // } else {
        //     // Send the voice command to Flask backend
        //     const response = await sendVoiceCommand(voice_command);
        //     document.getElementById('output').textContent = voice_command;
        // }

            
            // Send the voice command to Flask backend
            const response = await sendVoiceCommand(voice_command);
            document.getElementById('output').textContent = voice_command;
        };
  
        recognition.onerror = (event) => {
            console.error('Speech recognition error:', event.error);
        };
        
  } catch (error) {
      console.error('Error initializing speech recognition:', error);
  }
}
// let filePath="C:\\Users\\vaibh\\Music\\UnakkuThaan.mp3"
// function playMusic(filePath) {
//     const audio = new Audio(filePath);
//     audio.play();
// }

async function sendVoiceCommand(voice_command) {
  try {
      const response = await fetch('/process_voice_command', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({ voice_command })
      });

      if (!response.ok) {
          throw new Error('Failed to fetch response from server');
      }

      const responseData = await response.json();
      return responseData.response;
  } catch (error) {
      console.error('Error sending voice command:', error);
      return 'Error: Failed to process voice command';
  }
}
import sounddevice as sd
import wavio


#sampling frequency
freq = 48000
 
#duration of each clip
duration = 2

#this is the path to the file where we will store our positive wakeup input
path_to_store = "Positive_Wake_Samples/"

number_of_samples = 3

#I'm going to say "Hey Legion" about 100 times :')
for i in range(number_of_samples):

    # Start recorder with the given values 
    # of duration and sample frequency
    recording = sd.rec(int(duration * freq), 
                    samplerate=freq, channels=2)
    
    #give me a chance to speak my truth
    print(f'Collecting Sample Number: {i+1}')
    sd.wait()

    #write the file to the specified path
    wavio.write(path_to_store + "Legion_Wake" + str(i) + ".wav", recording, freq, sampwidth=2)
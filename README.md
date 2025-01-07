
# Simultaneous Instrument Music Generator

This Python program allows users to generate music with multiple instruments playing simultaneously. The generated music is saved as a MIDI file, and users can play the audio directly in their environment. It utilizes the `pretty_midi` library for MIDI creation and manipulation, and users can select instruments, set tempo, and generate melodies based on a predefined scale and rhythm pattern.

---

## Features

- **Multi-Instrument Support**:
  - Choose from a list of instruments (e.g., Piano, Violin, Guitar, Synth).
- **Melody Generation**:
  - Generates random melodies using the **C Major scale** and customizable rhythm patterns.
- **Customizable Settings**:
  - Set duration, tempo, and playback length.
- **MIDI Output**:
  - Saves the generated music to a `.mid` file.
- **Audio Playback**:
  - Play the generated music directly using the program.

---

## Prerequisites

### Python Libraries
The following libraries are required:
- `numpy`
- `pretty_midi`
- `IPython`

Install the dependencies using:
```bash
pip install numpy pretty_midi IPython
```

### Synthesizer for Playback
For audio playback, you may need a synthesizer backend like **FluidSynth**. Install it with:
```bash
pip install pyfluidsynth
```

Ensure you have a compatible sound font (`.sf2` file) installed. FluidSynth uses this file to render MIDI to audio.

---

## How to Use

### 1. Clone the Repository
```bash
git clone <repository_url>
cd <repository_folder>
```

### 2. Run the Program
Execute the script in a Python environment:
```bash
python music_generator.py
```

### 3. Select Instruments
The program will display a list of available instruments. Choose the desired instruments by entering their corresponding numbers (comma-separated).

### 4. Generate and Play Music
- The program generates a **1-minute MIDI file** with simultaneous instruments.
- You can play the first 10 seconds (or more) of the music directly in the environment.

### 5. Output File
The generated music is saved as `simultaneous_music.mid` in the current directory.

---

## Program Walkthrough

1. **Instrument Selection**:
   - Displays a list of General MIDI instrument names for the user to choose.
   - Selected instruments are used to create individual melodies.

2. **Melody Generation**:
   - Uses the C Major scale (`[60, 62, 64, 65, 67, 69, 71, 72]`) for note selection.
   - Rhythm patterns include quarter, half, three-quarter, and full notes.
   - Adds random gaps between notes for a natural flow.

3. **Simultaneous Playback**:
   - Each selected instrument plays its unique melody simultaneously.
   - Combines all melodies into a single MIDI file.

4. **Audio Playback**:
   - Converts MIDI to audio using FluidSynth and plays the generated waveform.

---

## Example Output

1. **Instrument Selection**:
   ```
   Available Instruments:
   1: Acoustic Grand Piano
   2: Electric Guitar (jazz)
   3: Violin
   4: String Ensemble 1
   5: Synth Lead
   Enter the numbers of the instruments you want (comma-separated): 1,3
   ```

2. **Generated Music**:
   - Instruments: Acoustic Grand Piano, Violin.
   - File saved as `simultaneous_music.mid`.

3. **Playback**:
   - Plays the first 10 seconds of the generated music.

---

## Customization

### 1. Modify the Scale
Change the `scale` variable to use a different set of MIDI pitches:
```python
scale = [60, 62, 64, 65, 67, 69, 71, 72]  # C Major scale
```

### 2. Adjust Rhythm Pattern
Modify the `rhythm_pattern` variable to change note durations:
```python
rhythm_pattern = [0.25, 0.5, 0.75, 1.0]  # Quarter, half, three-quarter, full notes
```

### 3. Change Tempo
Update the `tempo` variable to set the playback speed:
```python
tempo = 120  # Beats per minute
```

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for bug fixes, new features, or enhancements.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Built with the [`pretty_midi`](https://github.com/craffel/pretty-midi) library.
- Thanks to the creators of FluidSynth for audio playback capabilities.
- Inspired by the potential of programmatically generated music.

---

Enjoy creating your own multi-instrument music! 🎵

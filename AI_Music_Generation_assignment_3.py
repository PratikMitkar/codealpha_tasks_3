import numpy as np
import pretty_midi
from IPython.display import Audio

# Define constants
sampling_rate = 44100
tempo = 120  # Beats per minute
scale = [60, 62, 64, 65, 67, 69, 71, 72]  # C major scale (MIDI pitches)

# Instrument options (General MIDI program numbers)
instrument_choices = {
    "Acoustic Grand Piano": 0,
    "Electric Guitar (jazz)": 26,
    "Violin": 40,
    "String Ensemble 1": 48,
    "Synth Lead": 81,
}

def select_instruments():
    """
    Display instrument options and let the user select.
    """
    print("Available Instruments:")
    for idx, name in enumerate(instrument_choices.keys(), start=1):
        print(f"{idx}: {name}")

    selected_indices = input(
        "Enter the numbers of the instruments you want (comma-separated): "
    )
    selected_indices = [int(idx.strip()) for idx in selected_indices.split(",")]

    selected_instruments = []
    for idx in selected_indices:
        if 1 <= idx <= len(instrument_choices):
            selected_instruments.append(list(instrument_choices.keys())[idx - 1])
        else:
            print(f"Invalid selection: {idx}")
    return selected_instruments

def create_melody(scale, rhythm_pattern, duration_seconds):
    """
    Create a melody using a predefined scale and rhythm pattern for a given duration.
    """
    notes = []
    start_time = 0.0
    while start_time < duration_seconds:
        pitch = np.random.choice(scale)
        duration = np.random.choice(rhythm_pattern)
        velocity = np.random.randint(60, 127)
        end_time = start_time + duration

        if end_time <= duration_seconds:
            note = pretty_midi.Note(
                velocity=velocity,
                pitch=pitch,
                start=start_time,
                end=end_time,
            )
            notes.append(note)
        start_time = end_time + np.random.uniform(0.1, 0.3)  # Add gaps between notes
    return notes

def generate_music(output_file="user_music.mid", duration_seconds=60):
    """
    Generate music with multiple instruments playing simultaneously.
    """
    pm = pretty_midi.PrettyMIDI(initial_tempo=tempo)
    rhythm_pattern = [0.25, 0.5, 0.75, 1.0]  # Default rhythm pattern

    # User selects instruments
    selected_instruments = select_instruments()
    print(f"Selected Instruments: {selected_instruments}")

    for instrument_name in selected_instruments:
        program = instrument_choices[instrument_name]
        instrument = pretty_midi.Instrument(program=program, name=instrument_name)

        # Create a melody for this instrument
        melody_notes = create_melody(scale, rhythm_pattern, duration_seconds)
        instrument.notes.extend(melody_notes)
        pm.instruments.append(instrument)

    # Save the music to a MIDI file
    pm.write(output_file)
    print(f"Music saved to {output_file}")
    return pm

def play_music(pm, seconds=10):
    """
    Play the generated music as audio.
    """
    waveform = pm.fluidsynth(fs=sampling_rate)
    waveform_short = waveform[:seconds * sampling_rate]
    return Audio(waveform_short, rate=sampling_rate)

# Generate and play 1-minute music with simultaneous instruments
output_file = "simultaneous_music.mid"
pm = generate_music(output_file=output_file, duration_seconds=60)

# Play the first 10 seconds of the generated music
play_music(pm, seconds=60)

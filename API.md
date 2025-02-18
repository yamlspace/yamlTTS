# yamlTTS API Documentation

## Base URL
`http://localhost:5002`

## Endpoints

### 1. Text-to-Speech
**Endpoint:** `/api/tts`  
**Method:** POST  
**Content-Type:** application/json

#### Request Body Parameters
```json
{
    "text": "Text to synthesize",           // Required: Text to convert to speech
    "language": "en",                       // Required: Language code (e.g., "en", "es", "fr")
    "speaker_name": "Speaker 1",            // Optional: Name of the speaker voice to use
    "style_wav": "path/to/style.wav",      // Optional: Path to a style reference audio file
    "reference_wav": "path/to/ref.wav",    // Optional: For voice cloning, path to reference voice
    "reference_speaker_name": "Speaker 2"   // Optional: For multi-speaker models
}
```

#### Example Requests

1. Basic TTS:
```bash
curl -X POST "http://localhost:5002/api/tts" \
     -H "Content-Type: application/json" \
     -d '{
         "text": "Hello, world!",
         "language": "en"
     }'
```

2. With Speaker Selection:
```bash
curl -X POST "http://localhost:5002/api/tts" \
     -H "Content-Type: application/json" \
     -d '{
         "text": "Hello, world!",
         "language": "en",
         "speaker_name": "Speaker 1"
     }'
```

3. Voice Cloning:
```bash
curl -X POST "http://localhost:5002/api/tts" \
     -H "Content-Type: application/json" \
     -d '{
         "text": "Hello, world!",
         "language": "en",
         "reference_wav": "/path/to/reference.wav"
     }'
```

### 2. List Speakers
**Endpoint:** `/api/speakers`  
**Method:** GET

```bash
curl "http://localhost:5002/api/speakers"
```

### 3. List Languages
**Endpoint:** `/api/languages`  
**Method:** GET

```bash
curl "http://localhost:5002/api/languages"
```

### 4. Health Check
**Endpoint:** `/api/health`  
**Method:** GET

```bash
curl "http://localhost:5002/api/health"
```

## Response Format

### Success Response
```json
{
    "audio": "<base64_encoded_audio>",
    "message": "Success",
    "status": true
}
```

### Error Response
```json
{
    "message": "Error message details",
    "status": false
}
```

## Supported Languages
- English (en)
- Spanish (es)
- French (fr)
- German (de)
- Italian (it)
- Portuguese (pt)
- Polish (pl)
- Turkish (tr)
- Russian (ru)
- Dutch (nl)
- Czech (cs)
- Arabic (ar)
- Chinese (zh)
- Japanese (ja)
- Korean (ko)
- Hungarian (hu)
- Hindi (hi)

## Audio Output Format
- Format: WAV
- Sample Rate: 22050 Hz
- Channels: 1 (Mono)
- Bit Depth: 16-bit

## Error Codes
- 400: Bad Request - Missing or invalid parameters
- 404: Not Found - Resource not found
- 500: Internal Server Error - Server-side error

## Rate Limiting
The API currently does not implement rate limiting, but it's recommended to add delays between requests in production environments. 
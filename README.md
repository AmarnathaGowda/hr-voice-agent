# hr-voice-agent
This system lets you complete tasks using voice commands. It combines large language models (LLMs) with specialized microservices. It processes speech in real-time, routes tasks smartly, and ensures secure API use. It runs tasks in under 2 seconds while keeping enterprise security. Key features include hybrid NLP and containerized agents.

### Architecture ###
``` mermaid

    %%{init: {'theme': 'neutral', 'themeVariables': { 'primaryColor': '#F0F8FF'}}}%%
graph TD
    A[Web/Mobile App] -->|WebSocket + REST API| B[AWS API Gateway]
    
    subgraph AWS_Cloud
        B --> C[Voice Gateway]
        B --> D[HTTP Gateway]
        
        subgraph Voice_Processing
            C --> E[Amazon Transcribe 'STT']
            C --> F[Amazon Polly 'TTS']
            E -->|Text| G[Orchestrator Lambda]
            F -->|Audio| C
        end
        
        subgraph Core_Processing
            G --> H{Intent Classifier}
            H -->|Policy Query| I[Policy Agent]
            H -->|Leave Request| J[Leave Agent]
            
            I --> K[Qdrant Vector DB]
            I --> L[Amazon SageMaker 'BERT-Reranker']
            J --> M[BambooHR API]
            J --> N[Workday API]
        end
        
        subgraph Data_Layer
            K --> O[Policy Documents (S3)]
            P[Aurora PostgreSQL] -->|Employee Data| J
            Q[DynamoDB] -->|Session State| G
        end
        
        subgraph Monitoring
            R[Amazon CloudWatch] -->|Metrics| S[Auto Scaling]
            T[AWS X-Ray] -->|Traces| U[Service Lens Dashboard]
        end
        
        G -->|Logs| R
        I -->|Logs| R
        J -->|Logs| R
    end
    
    M -->|HRIS Integration| V[Enterprise VPN]
    N -->|HRIS Integration| V
    V --> W[(Corporate Network)]
    
    style A fill:#4CAF50,stroke:#388E3C
    style B fill:#2196F3,stroke:#0D47A1
    style G fill:#FF9800,stroke:#E65100
    style I fill:#9C27B0,stroke:#4A148C
    style J fill:#3F51B5,stroke:#1A237E


````
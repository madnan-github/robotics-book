import React, { useState, useEffect, useRef } from 'react';
import clsx from 'clsx';
import styles from './RagChatbot.module.css';

const API_BASE_URL = 'http://localhost:8080/api';

const RagChatbot = ({ visible = true }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!inputValue.trim() || isLoading) return;

    const userMessage = { id: Date.now(), text: inputValue, sender: 'user' };
    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);
    setError(null);

    try {
      const response = await fetch(`${API_BASE_URL}/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          query: inputValue,
          session_id: 'web-session-' + Date.now(),
        }),
      });

      if (!response.ok) {
        throw new Error(`API error: ${response.status} ${response.statusText}`);
      }

      const data = await response.json();

      const botMessage = {
        id: Date.now() + 1,
        text: data.response || 'Sorry, I could not understand your question.',
        sender: 'bot',
        confidence: data.confidence || null,
      };

      setMessages(prev => [...prev, botMessage]);
    } catch (err) {
      setError(err.message);
      const errorMessage = {
        id: Date.now() + 1,
        text: `Error: ${err.message}. Please make sure the backend server is running.`,
        sender: 'bot',
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  if (!visible) {
    return null;
  }

  return (
    <div className={styles.chatbotContainer}>
      {/* Chatbot Toggle Button */}
      <button
        className={clsx(styles.chatbotToggle, {
          [styles.chatbotToggleOpen]: isOpen,
        })}
        onClick={() => setIsOpen(!isOpen)}
        aria-label={isOpen ? 'Close chatbot' : 'Open chatbot'}
      >
        {isOpen ? '✕' : '🤖'}
      </button>

      {/* Chatbot Window */}
      {isOpen && (
        <div className={styles.chatbotWindow}>
          <div className={styles.chatbotHeader}>
            <h3>Robotics Learning Assistant</h3>
          </div>

          <div className={styles.chatbotMessages}>
            {messages.length === 0 ? (
              <div className={styles.welcomeMessage}>
                <p>Hello! I'm your Robotics Learning Assistant.</p>
                <p>Ask me anything about Physical AI & Humanoid Robotics!</p>
              </div>
            ) : (
              messages.map((message) => (
                <div
                  key={message.id}
                  className={clsx(styles.message, {
                    [styles.userMessage]: message.sender === 'user',
                    [styles.botMessage]: message.sender === 'bot',
                  })}
                >
                  <div className={styles.messageText}>{message.text}</div>
                  {message.confidence !== null && (
                    <div className={styles.confidenceScore}>
                      Confidence: {(message.confidence * 100).toFixed(1)}%
                    </div>
                  )}
                </div>
              ))
            )}
            {isLoading && (
              <div className={clsx(styles.message, styles.botMessage)}>
                <div className={styles.typingIndicator}>
                  <div className={styles.typingDot}></div>
                  <div className={styles.typingDot}></div>
                  <div className={styles.typingDot}></div>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          {error && (
            <div className={styles.errorMessage}>
              Error: {error}
            </div>
          )}

          <form onSubmit={handleSubmit} className={styles.chatbotInputForm}>
            <input
              type="text"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              placeholder="Ask about robotics..."
              className={styles.chatbotInput}
              disabled={isLoading}
            />
            <button
              type="submit"
              className={styles.chatbotSubmit}
              disabled={isLoading || !inputValue.trim()}
            >
              Send
            </button>
          </form>
        </div>
      )}
    </div>
  );
};

export default RagChatbot;
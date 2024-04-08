import React from 'react';
import { useState } from 'react';
import { InputTextarea } from 'primereact/inputtextarea';
import { Button } from 'primereact/button';
import { PostMethod } from '../api/http';

const interpreterAPI = process.env.REACT_APP_API_URL_INTERPRETER;

const Home = () => {

    const [codeText, setCodeText] = useState('')
    const [consoleText, setConsoleText] = useState('')
    
    const CompileInterpreter = async() => {
        const resp = await PostMethod(interpreterAPI+'interpreter', { code: codeText })
        await setConsoleText(resp?.console)
    }

    return (
        <div>
            <div style={{display: 'flex', marginTop: '5%'}}>
                <InputTextarea value={codeText} rows={15} cols={60} style={{marginBottom: '5%', marginRight: '2%'}} onChange={e => {setCodeText(e.target.value)}}/>
                <InputTextarea value={consoleText} rows={15} cols={60} style={{marginBottom: '5%', marginLeft: '2%'}} onChange={e => {setConsoleText(e.target.value)}}/>
            </div>
            <div style={{display: 'flex', marginBottom: '3%', justifyContent: 'center'}}>
                <Button label="INTERPRETAR" onClick={CompileInterpreter} style={{marginRight: '2%'}}/>
            </div>
        </div>
    );
};

export default Home;

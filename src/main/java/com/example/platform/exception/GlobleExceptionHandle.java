package com.example.platform.exception;

import com.example.platform.common.result;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseBody;

@ControllerAdvice
public class GlobleExceptionHandle {
    @ExceptionHandler(ServiceException.class)
    @ResponseBody
    public result handle(ServiceException se){
        return result.error(se.getCode(),se.getMessage());
    }
}

package com.example.simpleapi.controller;

import com.example.simpleapi.dao.UserDao;
import com.example.simpleapi.dto.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/")
public class UserController {

    @Autowired
    private UserDao userDao;

    @GetMapping
    public List<User> getAllUsers(){
        return userDao.findAll();
    }

    @PostMapping
    public User createUser(@RequestBody User user) {
        return userDao.save(user);
    }
}
